# Script:                       challenge309-AD-automation.ps1
# Author:                       Ethan Denny
# Date of latest revision:      3/10/2021
# Purpose:     This script will add a user to Active Directory



New-ADUser `
    -Name "Franz Ferdinand" `
    -SamAccountName "f.ferdinand" `
    -Company "GlobeX USA" `
    -City "Springfield" `
    -State "OR" `
    -Country "USA" `
    -OtherAttributes @{'title'="TPS Reporting Lead";'mail'="ferdi@GlobeXpower.com"}
