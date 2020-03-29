from flask import render_template, redirect


def load_contact_views(app, db):
    from contact_app.models import Contact
    from contact_app.forms import ContactCreateForm
    from contact_app.functions import enrich_details

    @app.route('/')
    def contact_list_view():
        all_contacts = Contact.query.all()
        return render_template('contact_app/contact_list.html', all_contacts=all_contacts)

    @app.route('/<int:contact_id>')
    def contact_detail_view(contact_id):
        contact = Contact.query.filter_by(id=contact_id).first()
        return render_template('contact_app/contact_details.html', contact=contact)

    @app.route('/add/<int:contact_id>', methods=['GET', 'POST'])
    def contact_create_view(contact_id):
        contact = Contact.query.filter_by(id=contact_id).first()  # checks already exists entry
        if contact:
            return "Contact with id {} already existing".format(contact_id)
        else:
            form = ContactCreateForm()
            form.id.default = contact_id
            if form.validate_on_submit():
                extra_info = enrich_details(email=form.data['email'])
                contact = Contact(
                    id=contact_id, email=form.data['email'],
                    first_name=form.data['first_name'], last_name=form.data['last_name'],
                    phone_number=form.data['phone_number'],
                    **extra_info
                )
                db.session.add(contact)
                db.session.commit()
                return redirect('/')
            return render_template('contact_app/contact_add.html', form=form, contact_id=contact_id)

    @app.route('/delete/<int:contact_id>', methods=['POST'])
    def contact_delete_view(contact_id):
        Contact.query.filter_by(id=contact_id).delete()
        db.session.commit()
        return redirect('/')

    @app.route('/search/<string:contact_name>')
    def contact_search_view(contact_name):
        from sqlalchemy import or_
        or_filters = [
            Contact.first_name.contains(contact_name),
            Contact.last_name.contains(contact_name),
            Contact.email.contains(contact_name)
        ]
        contacts = Contact.query.filter(or_(*or_filters))
        return render_template('contact_app/contact_search.html', all_contacts=contacts)
