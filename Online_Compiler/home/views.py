from django.shortcuts import render
from django.views import View
import traceback
from io import StringIO
from contextlib import redirect_stdout


def execute_code(code):
    
    try:
        # make instance for StringIO
        output_buffer = StringIO()
        # run the code
        with redirect_stdout(output_buffer):
            exec(code)
        output = output_buffer.getvalue()
    except Exception as e:
        # if there an error in excuting the code then this line with excute and printing the error massage 
        output = f"Error: {str(e)}\n{traceback.format_exc()}"
        
    # return the output
    return output

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    
    def post(self,request):
        codeareadata = request.POST['codearea']
        output = execute_code(codeareadata)
        return render(request, 'index.html', {"code": codeareadata, "output": output})