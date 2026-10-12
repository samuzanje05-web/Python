class Employee{
    private String emp_name;
    private int emp_id;
    private double salary;
    Employee(){
        emp_name="ABC";
        emp_id=101;
        salary=25000;
    }
    Employee(String emp_name){
        this.emp_name = emp_name;
    }
    Employee(String emp_name,int emp_id,double salary ){
     this.emp_name=emp_name;
     this.emp_id=emp_id;
     this.salary=salary;
    }
    void display(){
        System.out.println("the employee name:"+emp_name);
        System.out.println("the employee id :" +emp_id);
        System.out.println("the salary is:" +salary);
    }

    public class HR_System {
        public static void main(String[] args) {
        
    Employee e = new Employee("sammy");
    Employee e1 = new Employee("sammy",101,250000);
       e.display();
       e1.display();
}
}
}

