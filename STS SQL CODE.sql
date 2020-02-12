CREATE TABLE `sts`.`Customer`(
`Cust_id`  int PRIMARY KEY NOT NULL,
`Cust_name` varchar(45),
`Cust_type` varchar(45),
`Cust_ph`varchar(10) CHECK (length(Cust_ph=10)),
`Cust_age` int,
`Cust_pref`varchar(45));

CREATE TABLE `sts`.`Guest`(
`Cust_id`  int references Customer ,
`Guest_name` varchar(45) NOT NULL);

CREATE TABLE `sts`.`Rooms`(
`Floor` int,
`Room_id` int PRIMARY KEY UNIQUE NOT NULL,
`Room_price` int ,
`Room_type` varchar(45),
`Amenities` varchar(45));

CREATE TABLE `sts`.`Events`(
`Event_type`varchar(45),
`Event_name`varchar(45),
`No_of_part`int,
`Event_id` int UNIQUE NOT NULL PRIMARY KEY  ,
`Cust_id` int  references Customer ,
`Room_id` int references Rooms); 

CREATE TABLE `sts`.`Booking`(
`Book_desc` varchar(45),
`Book_id` int Primary key not null,
`Book_type` varchar(45),
`Date` date,
`Cust_id`  int references Customer,
`Room_id` int references Rooms);

CREATE TABLE `sts`.`Payment`(
`Pay_type` varchar(45),
`Cust_id`int references Customer,
`Pay_amount`int,
`Pay_id` int primary key ,
`Pay_date` date,
`Book_id` int references Booking);

#Question - 
select  distinct c.Cust_name from Customer c,Payment p,Guest g
where
p.Pay_amount in (select MAX(p2.Pay_amount) as MAX from Payment p2
where 
p2.Pay_date between '2017-01-01' and '2017-12-31'
and
p.Cust_id = c.Cust_id)
and
g.Cust_id = c.Cust_id;

