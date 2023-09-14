*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}        https://google.com
${BROWSER}    Chrome

*** Test Cases ***
Login
    Open Browser     https://opensource-demo.orangehrmlive.com/web/index.php/auth/login     Chrome
    Maximize Browser Window
    Sleep    5
    Input Text    username    Admin
    Input Password    password    admin123
    Click Button    xpath://button[@class = 'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']
    Sleep    5
    Close Browser

    

