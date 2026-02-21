from django.shortcuts import render, redirect
from .models import Student

# Show and Add student
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')

        Student.objects.create(
            name=name,
            email=email,
            course=course
        )
        return redirect('/')

    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})


# Delete student
def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')


# Edit student
def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})


# Update student
def update(request, id):
    student = Student.objects.get(id=id)

    student.name = request.POST.get('name')
    student.email = request.POST.get('email')
    student.course = request.POST.get('course')

    student.save()
    return redirect('/')