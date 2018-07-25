# reverseDictionary
Takes dictionary with arrays as values, and iterates over each array to create a new dictionary consisting of the arrays' values as keys and the original keys as the values of these new keys. Example is given in the JSON to demonstrate.

{
  "Cheese":["Motzerella", "Cheddar"]
  "Meat":["Pork", "Beef", "Chicken"]
}

Becomes:

{
  u'Pork': u'Meat',
  u'Motzerella': u'Cheese', 
  u'Cheddar': u'Cheese', 
  u'Chicken': u'Meat', 
  u'Beef': u'Meat'
}
