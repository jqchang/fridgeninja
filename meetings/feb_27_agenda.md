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

Models:
  Ingredient:
    name
    best_by
    rm_temp_stability
    refr_stability
    frz_stability
    created_at
    updated_at
