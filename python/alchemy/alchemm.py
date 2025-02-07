from sqlalchemy import * 

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

with engine.connect() as conn:
    conn.execute(
        text('create table some_table(x int, y int)')
     )
    
    conn.execute(
        text('insert into some_table(x, y) values(:x, :y)'),
        [{'x':50, "y":60},{'x':70,'y':80}]
    )

    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x}  y: {row.y}")
       

    conn.commit()

