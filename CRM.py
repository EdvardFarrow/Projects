class Lead:
  def __init__(self, lead_id, datetime, page, form_title, contacts, name):
    self.lead_id = lead_id
    self.datetime = datetime
    self.page = page
    self.form_title = form_title
    self.contacts = contacts
    self.name = name

  def to_dict(self):
    dictionary = {}
    dictionary['lead_id'] = self.lead_id
    dictionary['datetime'] = self.datetime
    dictionary['page'] = self.page
    dictionary['form_title'] = self.form_title
    dictionary['contacts'] = self.contacts
    dictionary['name'] = self.name
    return dictionary