from sqlalchemy import * 

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

with engine.begin() as conn:
    conn.execute(
        text('create table some_table(x int, y int)')
     )
    
    resutl = conn.execute(
        text('insert into some_table(x, y) values(:x, :y)'),
        [{'x':10, "y":20},{'x':30,'y':40}]
    )

    print(Result)
    

    conn.commit()

