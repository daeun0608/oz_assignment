-- 1. 생성 (CREATE)
-- (1) **`customers`** 테이블에 새 고객을 추가하세요.
insert into customers (customerNumber, customerName, contactLastName)
values (1, 'newName','newLastName');

-- (2) **`products`** 테이블에 새 제품을 추가하세요.
insert into products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
values ('S01','newProduct','Motorcycles','1:10','Min','This replica',5000,'40.00','50.00');

-- (3) **`employees`** 테이블에 새 직원을 추가하세요.
insert into employees (employeeNumber, lastName, firstName, extension, email, officeCode, jobTitle)
values (1000, '김', '다은', 'x2000', 'new@classicmodelcars.com', '0', 'student');

-- (4) **`offices`** 테이블에 새 사무실을 추가하세요.
insert into offices (officeCode, city, phone, addressLine1, country, postalCode, territory)
values ('0','San','010','address1','USA','123','NA');

-- (5) **`orders`** 테이블에 새 주문을 추가하세요.
insert into orders (orderNumber, orderDate, requiredDate, status, customerNumber)
values (200, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Shipped',1);

-- (6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요.
insert into orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
values (200,'S01',2,40.00,1);

-- (7) **`payments`** 테이블에 지불 정보를 추가하세요.
insert into payments (customerNumber, checkNumber, paymentDate, amount)
values (1,'A001', CURRENT_TIMESTAMP, 777.77);

-- (8) **`productlines`** 테이블에 제품 라인을 추가하세요.
insert into productlines (productLine) values ('newLine');

-- (9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.
insert into customers (customerNumber, customerName, contactLastName, country) values (2, 'newName2','newLastName2','newCountry');

-- (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
insert into products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
values ('S02','newProduct2','newLine','1:10','Min','This replica',5000,'40.00','50.00');



-- 2. 읽기 (READ)
-- (1) **`customers`** 테이블에서 모든 고객 정보를 조회하세요.
select * from customers;

-- (2) **`products`** 테이블에서 모든 제품 목록을 조회하세요.
select * from products;

-- (3) **`employees`** 테이블에서 모든 직원의 이름과 직급을 조회하세요.
select firstname, jobTitle from employees;

-- (4) **`offices`** 테이블에서 모든 사무실의 위치를 조회하세요.
select city, territory from offices;

-- (5) **`orders`** 테이블에서 최근 10개의 주문을 조회하세요.
select * from orders order by orderDate desc limit 10;

-- (6) **`orderdetails`** 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
select * from orderdetails where orderNumber=10100;

-- (7) **`payments`** 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
select * from payments where customerNumber=103;

-- (8) **`productlines`** 테이블에서 각 제품 라인의 설명을 조회하세요.
select productLine, textDescription from productlines;

-- (9) **`customers`** 테이블에서 특정 지역의 고객을 조회하세요.
select * from customers where country='France';

-- (10) **`products`** 테이블에서 특정 가격 범위의 제품을 조회하세요.
select * from products where buyPrice between 50 and 100;



-- 3. 갱신 (UPDATE)
-- (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
update customers set addressLine1='updateAdd' where customerNumber=1;

-- (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
update products set buyPrice='35.00' where productCode='S01';

-- (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
update employees set jobTitle='updateJob' where employeeNumber=1000;

-- (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
update offices set phone='010-111' where officeCode='0';

-- (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
update orders set status='Resolved' where orderNumber='200';

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
update orderdetails set quantityOrdered=12 where orderNumber=200;

-- (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
update payments set amount=1000 where customerNumber=1;

-- (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
update productlines set textDescription='업데이트되었다.' where productLine='newLine';

-- (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.
-- customers 테이블에는 이메일 컬럼이 없음 > employees 테이블?
update employees set email='update@classicmodelcars.com' where employeeNumber=1000;

-- (10) **`products`** 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
update products set buyPrice=case
when productCode='S01' then '10.00'
when productCode='S02' then '20.00' end
WHERE productCode IN ('S01', 'S02');



-- 4. 삭제 (DELETE)
-- (1) **`customers`** 테이블에서 특정 고객을 삭제하세요.
-- fk때문에 (5), (7)부터 시행
delete from customers where customerNumber=1;

-- (2) **`products`** 테이블에서 특정 제품을 삭제하세요.
delete from products where productCode='S01';

-- (3) **`employees`** 테이블에서 특정 직원을 삭제하세요.
delete from employees where employeeNumber=1000;

-- (4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.
delete from offices where officeCode='0';

-- (5) **`orders`** 테이블에서 특정 주문을 삭제하세요.
-- fk때문에 (6)부터 시행
delete from orders where orderNumber=200;

-- (6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.
delete from orderdetails where orderNumber=200;

-- (7) **`payments`** 테이블에서 특정 지불 내역을 삭제하세요.
delete from payments where customerNumber=1;

-- (8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.
-- fk때문에 (10)부터 실행
delete from productlines where productLine='newLine';

-- (9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.
-- safe모드를 끄지 않기위해 limit 추가
delete from customers where country='newCountry'
limit 130;

-- (10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
delete from products where productLine='newLine';