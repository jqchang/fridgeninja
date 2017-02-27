Feb 27:
2:00 pm - Wireframe of app
6:00 pm - Fully styled basic login/registration

Templates needed:
Login -- done but not styled
Success(myFridge) -- Shows inventory list of ingredients
  Add ingredient to inventory:
    a) by search - searches existing ingredients in database
    b) new - if can't find in list
    --
    c) user can enter a sell-by date if it's on the label
    d) optional: opened on
Recipes -- CRU(D) operations; delete may be optional

Current model concept:
- Database holds all currently registered ingredients
- User creates individual inventory entries, customized with more precise expiry info

Models:
  Ingredient:
    name
    rm_temp_stability
    refr_stability
    frz_stability
    ((How will we measure accuracy of this info? Rating system?))
    created_at
    updated_at

  Categories:
    name
    created_at
    updated_at

  User:
    first_name
    last_name
    email
    liked_categories
    disliked_categories
    created_at
    updated_at


  InventoryEntry:
    user_id (FK)
    ingredient_id (FK)
    best_by (datetime--user input)
    created_at (datetime auto)
    updated_at (datetime auto)

  Recipe:
    name
    creator
    ingredients (m2m)
    rating (separate model? FK?)

  Potluck/Event:
    name
    event_date
    creator
    members
