"""
WILL HAVE TO BE REWRITTEN FOR MULTITABLE RULES
"""
def query_to_representation(tables, query):
  table_name = query.get_From()[0]
  table = None
  for i in range(len(tables)):
    if tables[i].get_name() == table_name:
      table = tables[i] 
  header = table.get_schema()
  cols = query.get_Select()
  idxs = [header.index(c) for c in cols]
  return (table, idxs)
  
  

class Representation:
  def __init__(self, tables, query):
    (table, idxs) = query_to_representation(tables, query)
    self._table = table
    self._idxs = idxs


  def get_table(self):
    return self._table

  def get_idxs(self):
    return self._idxs

  def generateFuthark(self):
    """
    Generates Futhark code for the SQL Query 
    based on the internal Representation
    """
    select_header = "let select (cols : []i32) (row : []f32) : []f32 = \n"
    select_s1 = "  let f = (\i -> unsafe row[i])\n"
    select_s2 = "  in map f cols\n"
    select_from_header = "entry select_from_where (db : [][]f32) (cols : []i32) : [][]f32 =\n"
    result = "  map (select cols) db\n"
    fut_file = open("futhark/db_sel.fut", "w+")
    fut_file.write(select_header)
    fut_file.write(select_s1)
    fut_file.write(select_s2)
    fut_file.write("")
    fut_file.write(select_from_header)
    fut_file.write(result)


