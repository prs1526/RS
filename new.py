from flask import Flask ,render_template,url_for
app = Flask(__name__)

python = [{'topic':'Introduction',
            'url':'python_introduction'},
            {'topic':'Variable and Keywords',
            'url':'python_Variable_and_Keywords'},
            {'topic':'Types',
            'url':'python_Types'},
            {'topic':'Operators',
            'url':'python_Operators'},
            {'topic':'Expressions',
            'url':'python_Expressions'},
            {'topic':'Control Statements',
            'url':'python_Control_Statements'},
            {'topic':'Data_Structure',
            'url':'python_Data_Structure'},
            {'topic':'Functions',
            'url':'python_Functions'},
            {'topic':'Modules',
            'url':'python_Modules'},
            {'topic':'Packages',
            'url':'python_Packages'},
            {'topic':'Object Oriented Programming',
            'url':'python_Object_Oriented_Programming'},
            {'topic':'Exceptions',
            'url':'python_Exceptions'},
            {'topic':'Standard Library',
            'url':'python_Standard_Library'},
            {'topic':'Testing',
            'url':'python_Testing'}]
cpp =[
        {'topic':'Introduction',
        'url':'cpp_introduction'},
        {'topic':'Program Structure',
        'url':'cpp_program_structure'},
        {'topic':'Input and Output',
        'url':'cpp_input_output'},
        {'topic':'C++ Basics',
        'url':'cpp_basics'},
        {'topic':'Data Types',
        'url':'cpp_data_types'},
        {'topic':'Constants',
        'url':'cpp_constants'},
        {'topic':'Operators',
        'url':'cpp_operator'},
        {'topic':'Control Statements',
        'url':'cpp_control_statements'},
        {'topic':'Arrays',
        'url':'cpp_array'},
        {'topic':'Strings',
        'url':'cpp_strings'},
        {'topic':'Functions',
        'url':'cpp_functions'},
        {'topic':'Parameter Passing Techniques',
        'url':'cpp_parameter_passing'},
        {'topic':'Classes and Objects',
        'url':'cpp_class_object'},
        {'topic':'Constructor and Destructor',
        'url':'cpp_constructor_destructor'},
        {'topic':'Operator Overloading',
        'url':'cpp_op_overloading'},
        {'topic':'Type Conversion',
        'url':'cpp_type_conversion'},
        {'topic':'Inheritance',
        'url':'cpp_inheritance'},
        {'topic':'Types Of Inheritance',
        'url':'cpp_types_inheritance'},
        {'topic':'Polymorphism',
        'url':'cpp_polymorphism'},
        {'topic':'Abstract Class',
        'url':'cpp_abstact_class'},
        {'topic':'File Handling',
        'url':'cpp_file_handling'},
        {'topic':'Exception Handling',
        'url':'cpp_exception_handling'}
]
@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/signup")
def signup():
    return render_template('signup.HTML')


@app.route("/login")
def login():
    return render_template('LogIn.HTML')

@app.route("/courses")
def courses():
    return render_template('courses.html')


@app.route("/forum")
def forum():
    return render_template('forum.html')


@app.route("/survey")
def survey():
    return render_template('survey.html')

@app.route("/python_forum")
def py_forum():
    return render_template('python_forum.html')
#cpp Pages

@app.route("/cpp_introduction")
def cpp_introduction():
    return render_template('CPP/Introduction.html',topics=cpp)

@app.route("/cpp_program_structure")
def cpp_structure():
    return render_template('CPP/Structure.html',topics=cpp)

@app.route("/cpp_input_output")
def cpp_io():
    return render_template('CPP/Input_Output.html',topics=cpp)

@app.route("/cpp_basics")
def cpp_basics():
    return render_template('CPP/Basics.html',topics=cpp)

@app.route("/cpp_data_types")
def cpp_dataType():
    return render_template('CPP/Data_types.html',topics=cpp)

@app.route("/cpp_constants")
def cpp_constants():
    return render_template('CPP/Constants.html',topics=cpp)

@app.route("/cpp_operator")
def cpp_operator():
    return render_template('CPP/Operators.html',topics=cpp)

@app.route("/cpp_control_statements")
def cpp_control():
    return render_template('CPP/Control_Statements.html',topics=cpp)

@app.route("/cpp_array")
def cpp_array():
    return render_template('CPP/Arrays.html',topics=cpp)

@app.route("/cpp_strings")
def cpp_strings():
    return render_template('CPP/Strings.html',topics=cpp)

@app.route("/cpp_functions")
def cpp_functions():
    return render_template('CPP/Functions.html',topics=cpp)

@app.route("/cpp_parameter_passing")
def cpp_parameter():
    return render_template('CPP/Parameter_Passing.html',topics=cpp)

@app.route("/cpp_class_object")
def cpp_class_object():
    return render_template('CPP/Class_object.html',topics=cpp)

@app.route("/cpp_constructor_destructor")
def cpp_const_dest():
    return render_template('CPP/Constructor_Destructor.html',topics=cpp)

@app.route("/cpp_op_overloading")
def cpp_op_overloading():
    return render_template('CPP/Operator_Overloading.html',topics=cpp)

@app.route("/cpp_type_conversion")
def cpp_type_conversion():
    return render_template('CPP/Type_conversion.html',topics=cpp)

@app.route("/cpp_inheritance")
def cpp_inheritance():
    return render_template('CPP/Inheritance.html',topics=cpp)

@app.route("/cpp_types_inheritance")
def cpp_types_inheritance():
    return render_template('CPP/Types_Inheritance.html',topics=cpp)

@app.route("/cpp_polymorphism")
def cpp_poly():
    return render_template('CPP/Polymorphism.html',topics=cpp)

@app.route("/cpp_abstact_class")
def cpp_abstract_class():
    return render_template('CPP/Abstract_class.html',topics=cpp)

@app.route("/cpp_file_handling")
def cpp_file():
    return render_template('CPP/File_Handling.html',topics=cpp)

@app.route("/cpp_exception_handling")
def cpp_exception_handling():
    return render_template('CPP/Exception_Handling.html',topics=cpp)

# python pages

@app.route("/python_introduction")
def py_introduction():
    return render_template('F_python/Introduction.html',topics=python)

@app.route("/python_Variable_and_Keywords")
def py_Var_Key():
    return render_template('F_python/Variables_Keywords.html',topics=python)

@app.route("/python_Types")
def py_types():
    return render_template('F_python/Types.html',topics=python)

@app.route("/python_Operators")
def py_operators():
    return render_template('F_python/Operators.html',topics=python)

@app.route("/python_Expressions")
def py_expressions():
    return render_template('F_python/Expressions.html',topics=python)

@app.route("/python_Control_Statements")
def py_cont_stat():
    return render_template('F_python/Control_Statements.html',topics=python)

@app.route("/python_Data_Structure")
def py_ds():
    return render_template('F_python/Data_Structures.html',topics=python)

@app.route("/python_Functions")
def py_functions():
    return render_template('F_python/Functions.html',topics=python)

@app.route("/python_Modules")
def py_mpdules():
    return render_template('F_python/Modules.html',topics=python)

@app.route("/python_Packages")
def py_packages():
    return render_template('F_python/Packages.html',topics=python)

@app.route("/python_Object_Oriented_Programming")
def py_oop():
    return render_template('F_python/oop.html',topics=python)

@app.route("/python_Exceptions")
def py_exceptions():
    return render_template('F_python/Exception.html',topics=python)

@app.route("/python_Standard_Library")
def py_st_lib():
    return render_template('F_python/Standard_Library.html',topics=python)

@app.route("/python_Testing")
def py_testing():
    return render_template('F_python/Testing.html',topics=python)




if __name__ == '__main__':
    app.run(debug=True)
