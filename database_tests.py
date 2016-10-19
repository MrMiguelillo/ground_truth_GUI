import database

tables = ['sellos', 'documentos']
db = database.Database('docs_osborne', 'testuser', 'test123', tables)
db.load_seals()

a = 0
