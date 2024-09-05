from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import logging

logger = logging.getLogger(__name__)
 
@csrf_exempt
def index(request):
    def gurumishaTPO():
        # Retrieve session variables, or initialize them if not already set
        plate_number = request.session.get('plate_number')
        chassis_number = request.session.get('chassis_number')
        vehicle_make = request.session.get('vehicle_make')
        valid_license = request.session.get('valid_license')
        
        if text == '3*1':
            response = "CON Enter Vehicle Details:\n"
            response += "1. Enter Plate Number\n"
            return HttpResponse(response, content_type='text/plain')
        
        elif text.startswith('3*1*1'):
            plate_number = text.split('*')[-1]
            request.session['plate_number'] = plate_number  # Store in session
            response = "CON Enter Chassis Number:\n"
            return HttpResponse(response, content_type='text/plain')
        
        elif text.startswith('3*1*2'):
            chassis_number = text.split('*')[-1]
            request.session['chassis_number'] = chassis_number  # Store in session
            response = "CON Select Vehicle Make:\n"
            response += "1. Toyota\n2. Honda\n3. Ford\n4. Other"
            return HttpResponse(response, content_type='text/plain')
        
        elif text.startswith('3*1*3'):
            vehicle_make_option = text.split('*')[-1]
            if vehicle_make_option == '4':  # Other
                response = "CON Enter Vehicle Make:"
                return HttpResponse(response, content_type='text/plain')
            else:
                vehicle_make = ["Toyota", "Honda", "Ford"][int(vehicle_make_option) - 1]
                request.session['vehicle_make'] = vehicle_make  # Store in session
                response = "CON Valid Driving License (Yes or No):"
                return HttpResponse(response, content_type='text/plain')
        
        elif text.startswith('3*1*4'):
            if request.session.get('vehicle_make') is None:  # Custom make entered by user
                vehicle_make = text.split('*')[-1]
                request.session['vehicle_make'] = vehicle_make  # Store in session
            response = "CON Valid Driving License (Yes or No):"
            return HttpResponse(response, content_type='text/plain')
        
        elif text.startswith('3*1*5'):
            valid_license = text.split('*')[-1].lower() == 'yes'
            request.session['valid_license'] = valid_license  # Store in session
            
            # Log the collected data
            logger.debug(f"Plate Number: {request.session.get('plate_number')}")
            logger.debug(f"Chassis Number: {request.session.get('chassis_number')}")
            logger.debug(f"Vehicle Make: {request.session.get('vehicle_make')}")
            logger.debug(f"Valid Driving License: {request.session.get('valid_license')}")
            
            response = "END Thank you for providing your vehicle details. We will process your insurance request."
            return HttpResponse(response, content_type='text/plain')

        return HttpResponse("END Unexpected input. Please try again.", content_type='text/plain')
    
    def motor_Commercial():
        print('You are now in Motor Commercial')
        return JsonResponse({'success': 'You are now accessing Motor Commercial'}, status=500)
    
    def tpo():
        print('You are now in Third Party Insurance')
        return JsonResponse({'success': 'You are now accessing TPO Insurance'}, status=500)


    def comprehensive_insurance():
        print('You are now in Comprehensive Insurance')
        return JsonResponse({'success': 'You are now accessing Comprehensive Insurance'}, status=500)
    
    def life_insurance():
        print('You are now in Group Life Insurance')
        return JsonResponse({'success': 'You are now accessing Group Life Insurance'}, status=500)
    

        
    if request.method == 'POST':
        session_id = request.POST.get("sessionId", None)
        serviceCode = request.POST.get("serviceCode", None)
        phone_number = request.POST.get("phoneNumber", None)
        text = request.POST.get("text", "default")
        
        logger.debug(f"Received POST request: sessionId={session_id}, serviceCode={serviceCode}, phoneNumber={phone_number}, text={text}")

        if not all([session_id, serviceCode, phone_number]):
            logger.error('Missing parameter')
            return JsonResponse({'error': 'Missing parameter'}, status=400)

        if text == '':
            response = "CON What would you want to check \n"
            response += "1. My Account \n"
            response += "2. My phone number \n"
            response += "3. Access Monarch Insurance Products."
        elif text == '1':
            response = "CON Choose account information you want to view \n"
            response += "1. Account number"
        elif text == '2':
            response = f"END Your phone number is {phone_number}\n"
        elif text == '3':
            response = "CON What insurance cover would you like?\n"
            response += "1. Gurumisha Third Party Only Cover \n"
            response += "2. Motor Commercial Insurance \n"
            response += "3. Third Party Only Cover \n"
            response += "4. Comprehensive Insurance \n"
            response += "5. Group Life Insurance \n"
        elif text == "3*1":
            response = "END You have chosen Commercial Motor Insurance"
            return gurumishaTPO()
        elif text == "3*2":
            response = "END You have chosen  Motor Commercial Only Cover"
            return motor_Commercial()

        elif text == "3*3":
            response = "END You have chosen Third Party Only Cover"
            return tpo()
        elif text == "3*4":
            response = "END You have chosen Comprehensive Insurance"
            return comprehensive_insurance()
        elif text == "3*5":
           return life_insurance()
            
        elif text == '1*1':
            accountNumber = "ACC1001"
            response = f"END Your account number is {accountNumber}"
        else:
            response = "END Invalid choice"

        return HttpResponse(response, content_type='text/plain')

    return HttpResponse("This endpoint only accepts POST requests", status=405)
