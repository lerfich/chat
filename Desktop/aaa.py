import sqlite3

def sqlite3_simple_example_create_db():
    """
    Функция для создания базы данных с использование СУБД sqlite3
    """
    # Соединяемся с базой данных, если базы данных нет создается новая с таким именем
    con = sqlite3.connect('./test_data/PyScientist_base.db')

    # Создаем объект курсора
    cur = con.cursor()
    # Создаем таблицу если таблицы не существует
    cur.execute('CREATE TABLE IF NOT EXISTS core_fes(Well TEXT, '
                                                    'Sample TEXT, '
                                                    'Porosity FLOAT, '
                                                    'Swr FLOAT, '
                                                    'Permeability FLOAT)')
    # Добавляем данные в таблицу
    cur.execute('INSERT INTO core_fes VALUES("Yellow snake creek", "Sample #666", 25.6, 38, 16)')
    # Закрываем курсор
    data = ["Green snake creek", "Sample #333", 24, 20, 34]
    big_data = []
    data1 = ["Brown snake creek", "Sample #111", 15, 2, 32]
    data2 = ["Dark snake creek", "Sample #222", 20, 17, 55]
    big_data.append(data1)
    big_data.append(data2)

    cur.execute('INSERT INTO core_fes VALUES(?, ?, ?, ?, ?)', data)
    for data_unit in big_data:
        cur.execute('INSERT INTO core_fes VALUES(?, ?, ?, ?, ?)', data_unit)
    cur.close()
    # Подтверждаем внесение данных в таблицу (другими словами записываем изменения)
    con.commit()
####
####
####
####
def sqlite3_simple_read_db(data_base, table, column_name = None):
    # Соединяемся с базой данных, если базы данных нет создается новая с таким именем
    con = sqlite3.connect(data_base)
    # Создаем объект курсора
    cur = con.cursor()
    query_columns  = 'pragma table_info('+table+')'
    cur.execute(query_columns)
    columns_description = cur.fetchall()
    columns_names = []
    for column in columns_description:
        columns_names.append(column[1])

    if column_name is None:
        query = 'SELECT * FROM '+table
        cur.execute(query)
        data = cur.fetchall()
    else:
        query = 'SELECT '+column_name+' FROM '+table
        cur.execute(query)
        data = cur.fetchall()
        new_data = []
        for element in data:
            new_data.append(element[0])
        data = new_data
        del(new_data)
    print_data_2d(columns_names, data)
    cur.close()
    con.close()
####
####
####
####
def sqlite3_simple_delete_table(data_base, table):
    # Соединяемся с базой данных, если базы данных нет создается новая с таким именем
    con = sqlite3.connect(data_base)
    # Создаем объект курсора
    cur = con.cursor()
    query = 'DROP TABLE IF EXISTS '+table
    cur.execute(query)
    cur.close()
    con.close()
####
####
####
####
def sqlite3_update_record(data_base, table, id_column, record_id, param_column, param_val):
    # Соединяемся с базой данных, если базы данных нет создается новая с таким именем
    con = sqlite3.connect(data_base)
    # Создаем объект курсора
    cur = con.cursor()
    query = 'UPDATE '+table+' SET '+param_column+'='+str(param_val)+' WHERE '+id_column+" = '"+str(record_id)+"'"
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()
####
####
####
####
def sqlite3_simple_delete_record(data_base, table, id_column, record_id):
    # Соединяемся с базой данных, если базы данных нет создается новая с таким именем
    con = sqlite3.connect(data_base)
    # Создаем объект курсора
    cur = con.cursor()
    query = 'DELETE FROM '+table+' WHERE '+id_column+" = '"+record_id+"'"
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()
####
####
####
####

if __name__ == '__main__':
    data_base = /.#adress
    table = 'core_fes'
    id_column = 'Sample'
    record_id = 'Sample #333'
    param_column = 'Porosity'
    param_val = 9

#sqlite3_simple_example_create_db()
#sqlite3_simple_delete_table(data_base, table)
#sqlite3_simple_delete_record(data_base,table, id_column, record_id)
sqlite3_update_record(data_base, table, id_column, record_id, param_column, param_val)
sqlite3_simple_read_db(data_base, table)
