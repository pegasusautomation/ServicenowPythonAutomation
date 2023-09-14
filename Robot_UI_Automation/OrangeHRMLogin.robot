*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}        https://google.com
${BROWSER}    Chrome

*** Test Cases ***
Login
    Open Browser     https://opensource-demo.orangehrmlive.com/web/index.php/auth/login     Chrome
    LoginToApplication
    Close Browser
*** Keywords ***
LoginToApplication
    Maximize Browser Window
    Sleep    5
    Input Text    username    ${URL}
    Input Password    password    ${BROWSER}
    Click Button    xpath://button[@class = 'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']

    

