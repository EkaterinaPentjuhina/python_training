Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>, <middlename>, <nickname>, <title>, <company>, <homephone>, <mobilephone>, <workphone>, <phone2>, <email>, <homepage>, <address>
  When I add the contact to the list
  Then the new contact list is equal to the old list with added contact

  Examples:
  | firstname  | lastname  | middlename  | nickname  | title  | company  | homephone  | mobilephone  | workphone  | phone2  | email      | homepage  | address  |
  | firstname1 | lastname1 | middlename1 | nickname1 | title1 | company1 | 1111-1111  | 111-11-1111  | 111-11-11  | 11-111  | 1@mail.ru  | 1.net     | address1 |



Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact


Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given new contact's data
  When I modify the contact's properties
  Then the new contact list is equal to the old contact list with the modified contact
