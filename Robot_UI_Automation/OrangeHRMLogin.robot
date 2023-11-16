*** Settings ***
Library  SeleniumLibrary
Resource    Downloadfile.robot

*** Test Cases ***
Login
    ${value}    download file
    Close Browser


