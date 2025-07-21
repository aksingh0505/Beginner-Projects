def calculate_bmi(weight,height):
    bmi=weight/(height**2)
    return bmi

def classification_bmi(bmi):
    if bmi<18.5:
        return 'underweight'
    elif 18.5<= bmi <25:
        return 'normal'
    elif 25 <= bmi <30:
        return 'overweight'
    else:
        return 'obesity'
    
def bmi_calc():
    weight=float(input('Enter the weight in KG. '))
    height=float(input('Enter the height in Meters. '))

    if weight<=0 or height <=0:
        print('Enter right value')
        return
    
    bmi=calculate_bmi(weight,height)
    category=classification_bmi(bmi)

    print('\nYour BMI is. ',round(bmi,2))
    print('Your Classification is. ',category)
    except ValueError:
        print('Enter valid numeric values')

bmi_calc()
