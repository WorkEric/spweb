# Spweb project design docs

This document focus on the spweb project workflow and database design


## Business requirement 

We are the ToB company website, based on company business, we are focus on the chatbot. 

* Main page
* Domain
* Price
* Career
* Login / Logout


<br>

## Database UML


<br>

## Database Design

Database including business Domain, price, user


### 1. Table `template_category`

This table focus on the template category

| Field | Type | Note | Description |
|---|---|---|---|
| id | int(11) | PK, AUTO_INCREMENT |
| name | varchar(255)| UNIQ | |
| order_number | int(11) |  | same order number would be list by created_at time |
| created_at | datetime(6) |  |  |
| updated_at | datetime(6) |  |  |


### 2. Table `template_content`

This table focus on the template content

| Field | Type | Note | Description |
|---|---|---|---|
| id | int(11) | PK, AUTO_INCREMENT |
| title | varchar(255)| | content title name |
| image | varchar(1024) |  | image of picture |
| description | longtext |  | description of picture | 
| created_at | datetime(6) |  |  |
| updated_at | datetime(6) |  |  |


### 3. Table `template_category_content`

Since template category and template content are many to many relation, so we use the transaction table here.

| Field | Type | Note | Description |
|---|---|---|---|
| id | int(11) | PK, AUTO_INCREMENT |
| template_category_id | int(11)| ForeignKey to template_category.id | |
| template_content_id | int(11) | ForeignKey to template_content.id |  |  
| created_at | datetime(6) |  |  |
| updated_at | datetime(6) |  |  |


### 4. Table `price_plan`

Table for price plan 

| Field | Type | Note | Description |
|---|---|---|---|
| id | int(11) | PK, AUTO_INCREMENT |
| name | varchar(255)| UNIQ |  |
| short_description | longtext| |  |
| long_description | longtext| |  |
| created_at | datetime(6) |  |  |
| updated_at | datetime(6) |  |  |


### 5. Table `price_payment`

Table for price payment value and duration

| Field | Type | Note | Description |
|---|---|---|---|
| id | int(11) | PK, AUTO_INCREMENT |
| price_plan_id |  int(11) |  ForeignKey to price_plan.id | |
| price_type | varchar(255)| | Free, Lite, Standard and Plus |
| value | int(11) | Money only integer, no conside float. |  |  
| duration | int(11) |  | unit: month | 
| created_at | datetime(6) |  |  |
| updated_at | datetime(6) |  |  |



### 6. Table `price_feature`

Table for price plan

| Field | Type | Note | Description |
|---|---|---|---|
| id | int(11) | PK, AUTO_INCREMENT |
| name | varchar(255)| |  |
| description | longtext |  | For tooltip |  
| created_at | datetime(6) |  |  |
| updated_at | datetime(6) |  |  |


### 7. Table `price_payment_feature`

Since price_plan and price_feature are many to many relation, so we use the transaction table here.

| Field | Type | Note | Description |
|---|---|---|---|
| id | int(11) | PK, AUTO_INCREMENT |
| price_plan_id | int(11)| ForeignKey to price_plan.id | |
| price_feature_id | int(11) |  ForeignKey to price_feature.id |  |  
| value | varchar(255) | | payment and feature value: yes/no/number/unlimit |
| created_at | datetime(6) |  |  |
| updated_at | datetime(6) |  |  |


### 8. Table `sp_user`

Table for price plan 

| Field | Type | Note | Description |
|---|---|---|---|
| id | int(11) | PK, AUTO_INCREMENT |
| username | varchar(255)| UNIQ |  |
| first_name | varchar(255) |  |  |  
| last_name | varchar(255) |  |  |
| email | varchar(255)| UNIQ |  |
| company | varchar(255) | | |
| company_url | varchar(1024) | | | 
| phone | varchar(255)| UNIQ |  |
| avatar | varchar(1024)| | image of people |
| activated | tinyint(1)| | Boolean: user is activated or not |
| whitelisting | tinyint(1)| | Boolean: if this user is admin user |
| created_at | datetime(6) |  |  |
| updated_at | datetime(6) |  |  |

### 9. Table 'user_price_payment'

Table for user select plan 

| Field | Type | Note | Description |
|---|---|---|---|
| id | int(11) | PK, AUTO_INCREMENT |
| sp_user_id | int(11)| ForeignKey to user.id |  |
| price_payment_id | int(11)| ForeignKey to price_payment.id |  |
| start_at | datetime(6) |  |  |
| end_at | datetime(6) |  |  |
| created_at | datetime(6) |  |  |
| updated_at | datetime(6) |  |  |
