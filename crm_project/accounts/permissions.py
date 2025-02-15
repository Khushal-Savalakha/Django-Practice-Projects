from django.contrib.auth.mixins import UserPassesTestMixin

class HRRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'HR'

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'Admin'

class ContractorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'Contractor'

class EmployeeRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'Employee'
