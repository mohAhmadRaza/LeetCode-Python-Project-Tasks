class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Create a dictionary to map each employee's ID to the Employee object
        employee_map = {employee.id: employee for employee in employees}
        
        # Define the DFS function to calculate total importance
        def DFS(emp_id):
            curr_employee = employee_map[emp_id]
            total_importance = curr_employee.importance
            for subordinate_id in curr_employee.subordinates:
                total_importance += DFS(subordinate_id)
            return total_importance
        
        # Start DFS with the given employee ID
        return DFS(id)
