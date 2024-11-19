create table productos(
id serial primary key,
descripcion varchar(500) not null,
precio float not null,
fecha_guardado date default current_date
)
select * from productos
order by precio 
limit 10
delete from productos
SELECT COUNT(*) FROM productos