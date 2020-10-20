*** Settings ***
Library  SeleniumLibrary
Library  ../pages/HomePage.py
Library  ../pages/ProductPage.py


*** Keywords ***

that the informed region is eligible
    Gate Yes
    Set Test Variable  ${ADDRESS}  Avenida tiradentes, Luz, São Paulo -SP, Brasil
    Informe Adress  ${ADDRESS} 

the user select amount of products
    Page Should Contain  Cervejas
    Select Product
    Add Amount Product
    Add Products
    
the purchase price must be updated in the cart
    Calculate Cart