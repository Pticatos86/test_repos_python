from Args_kwargs_oop.homework_args_and_oop import MafiaEmployee

if __name__ == '__main__':
    anastasiya = MafiaEmployee('management', 'director', 'Anastasiya', 'Bondarenko',
                               36, 1500)
    volodymyr = MafiaEmployee('security', 'head of security', 'Volodymyr',
                              'Kovalenko', 45, 1000)

    print(f"Information about employee - {anastasiya}")
    print(f"Information about employee - {volodymyr}")
    print(f"Calculated salary of {anastasiya.job_title} {anastasiya.name} is {anastasiya.calculate_salary()}")
    print(f"Calculated salary of {volodymyr.job_title} {volodymyr.name} is {volodymyr.calculate_salary()}")
    volodymyr.change_salary = 1200
    print(
        f"Salary of {volodymyr.job_title} {volodymyr.name} has changed. New salary is {volodymyr.calculate_salary()}")
    anastasiya.change_surname = "Pshenichna"
    print(f"{anastasiya.job_title} {anastasiya.name} has married. Her new surname is {anastasiya.change_surname}")
