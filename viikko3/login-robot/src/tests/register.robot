*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  mirat  mira1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  mira1234
    Output Should Contain  Username is already in use

Register With Too Short Username And Valid Password
    Input Credentials  mo  mira1234
    Output Should Contain  Username is too short

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  mira12  mira1234
    Output Should Contain  Username must contain only letters from a-z

Register With Valid Username And Too Short Password
    Input Credentials  mira  k92
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  mira  kallekalle
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command

