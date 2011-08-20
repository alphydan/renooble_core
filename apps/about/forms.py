class ContactForm(forms.Form):
    POSSIBLE_SUBJECTS = (
            ('support', 'Support / Volunteer for Re.nooble'),
            ('suggestion', 'Suggestion to the re.nooble project'),
            ('supplier', 'New entry request for suppliers'),
            ('other', 'Hm, my subject is not in the list'),
            )

    subject = forms.CharField(max_length=15, choices = POSSIBLE_SUBJECTS)
    message = forms.CharField()
    sender = forms.EmailField()
