create schema ana_rodrigues

create table ana_rodrigues.usuario(
	id_user int PRIMARY KEY NOT NULL,
	nome varchar(50) NOT NULL,
	sobrenome varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
	bairro varchar (50) NOT NULL,
	data_de_nascimento date NOT NULL);


create table ana_rodrigues.cartao(
	id_cartao int PRIMARY KEY NOT NULL,
	id_user int FOREIGN KEY references ana_rodrigues.usuario(id_user),
	creditos decimal (25,2) NOT NULL,
	tipo varchar(15) NOT NULL,
	data_emissao date NOT NULL);

create table ana_rodrigues.motorista(
	id_motorista int PRIMARY KEY NOT NULL,
	numero_CNH int not null,
	nome varchar(50) not null,
	sobrenome varchar (50) not null,
	data_nascimento date 
);

create table ana_rodrigues.onibus(
	placa int PRIMARY KEY NOT NULL,
	linha int NOT NULL,
	modelo varchar(40) not null,
	data_fabricacao date not null,
	id_motorista int foreign key references ana_rodrigues.motorista(id_motorista) not null, 
);