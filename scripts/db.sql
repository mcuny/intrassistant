create database intra;
create user admin with password 'mdp12345';

alter role admin set client_encoding to 'utf8';
alter role admin set default_transaction_isolation to 'read committed';
alter role admin set timezone to 'UTC';

grant all privileges on database intra to admin;
