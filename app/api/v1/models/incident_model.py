incidents = []

class IncidentModel():

    def __init__(self):
        self.data = incidents


    def get_all_records(self):
        return self.data

    def get_single_record(self,id):
        
        incident = [incident for incident in incidents
                   if incident["id"] == id]
        return incident
