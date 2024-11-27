SELECT * from customer_details;

/*
create table IF NOT EXISTS customer_details(
    customer_id int auto_increment primary key,
    product_name varchar(333),
    price decimal(10,2)
    );

insert into customer_details (product_name, price) values
    ("laptop", 45000.00),
    ("mobile", 5000.00),
    ("desktop", 8000.00),
    ("smartwatch", 2500.00),
    ("headphones", 1000.00),
    ("charger", 800.00)
;

create table order_details(
    id int,
    customer_name varchar(333),
    place varchar(33),
    phone int(10),
    foreign key (id) references customer_details(customer_id)
);

insert into order_details values
    (1,"John Doe","New York",123456780),
    (2,"Jane Smith","Los Angeles",987654320),
    (3,"Bob Johnson","Chicago",555555555),
    (4,"Alice Davis","San Francisco",444444444),
    (5,"Charlie Brown","Boston",666666666);
    */




