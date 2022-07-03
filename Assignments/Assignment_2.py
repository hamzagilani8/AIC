# ********** Marks Sheet ********
# input details
print('************ Enter Details **********')
name = input('Enter Name: ')
Class = input('Class: ')
roll_num = input('Roll Number: ')


# Input values
print('************ Enter Marks **********')
phy_max = input('Maximum Marks in Physics: ')
phy_obt = input('Obtaied Marks in Physics: ')
chem_max = input('Maximum Marks in Chemistry: ')
chem_obt = input('Obtaied Marks in Chemistry: ')
bio_max = input('Maximum Marks in Biology: ')
bio_obt = input('Obtaied Marks in Biology: ')
isl_max = input('Maximum Marks in Islamiat: ')
isl_obt = input('Obtaied Marks in Islamiat: ')
urdu_max = input('Maximum Marks in Urdu: ')
urdu_obt = input('Obtaied Marks in Urdu: ')

# ************** Finding Percentage ********************
phy_per = (float(phy_obt)/float(phy_max))*100
chem_per = (float(chem_obt)/float(chem_max))*100
bio_per = (float(bio_obt)/float(bio_max))*100
isl_per = (float(isl_obt)/float(isl_max))*100
urdu_per = (float(urdu_obt)/float(urdu_max))*100


# ***************** Grading function *******************
def grading(sub_per):
    if sub_per >= 80:
        return 'A'
    elif sub_per >= 70 and sub_per <= 79.99:
        return 'B'
    elif sub_per >= 60 and sub_per <= 69.99:
        return 'C'
    elif sub_per >= 33 and sub_per <= 59.99:
        return 'D'
    else:
        return 'FAIL'

# ************ Grading *******************************
phy_grade = grading(phy_per)
chem_grade = grading(chem_per)
bio_grade = grading(bio_per)
isl_grade = grading(isl_per)
urdu_grade = grading(urdu_per)

# ************ Totals ********************************
total_marks = (int(phy_max)) +(int(chem_max)) +(int(bio_max)) +(int(isl_max)) +(int(urdu_max))
obt_marks = (float(phy_obt)) +(float(chem_obt)) +(float(bio_obt)) +(float(isl_obt)) +(float(urdu_obt))
total_per = (float(obt_marks)/float(total_marks))*100

# *************** Result card **************************
print('****** SCHOOL Result Card *****')
print('********** ' + 'Class: ' + Class +' *********')
print(' ')
print('NAME: ' + name)
print('Roll # ' + roll_num)
print(' ')
print('SUBJECT       ' + 'Max Marks' + '    ' + 'Obtained Marks' + '    ' + 'Grade')
print('Physics       ' + '   ' + phy_max + '              ' + phy_obt + '          ' + grading(phy_per))
print('Chemistry     ' + '   ' + chem_max + '              ' + chem_obt + '          ' + grading(chem_per))
print('Biology       ' + '   ' + bio_max + '              ' + bio_obt + '          ' + grading(bio_per))
print('Islamiat      ' + '   ' + isl_max + '              ' + isl_obt + '          ' + grading(isl_per))
print('Urdu          ' + '   ' + urdu_max + '              ' + urdu_obt + '          ' + grading(urdu_per))
print('_____________________________________________________')
print(' ')
print('Total Marks    ' + '| ' + str(total_marks))
print('Obtained Marks ' + '| ' + str(obt_marks))
print('Overall Grade  ' + '| ' + grading(total_per))
print(' ')
print('_____________________________________________________')
print(' ')

if grading(phy_per) == 'FAIL' or grading(chem_per) == 'FAIL' or grading(bio_per) == 'FAIL' or grading(isl_per) == 'FAIL' or grading(urdu_per) == 'FAIL':
    print('You are fail in any subject(S), please make a reattempt and PASS to get promoted')
else:
    print('CONGRATULATIONS YOU ARE PROMOTED TO NEXT CLASS')

print(' ')
