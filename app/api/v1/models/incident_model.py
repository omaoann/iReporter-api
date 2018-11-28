from datetime import datetime

incidents = []

class IncidentModel():

    def __init__(self):
        self.data = incidents


    def get_all_records(self):
        return self.data

    def get_single_record(self,id):
        """This method fetches a single record given the id"""

        incident = [incident for incident in incidents
                   if incident["id"] == id]
        return incident


    def save(self,createdBy,record_type,location,comment ):
        """This method to create and save a dict object"""
        
        id = len(self.data)+1
        status = 'Draft'
        date = datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
        details = {
            'id' : id,
            'createdOn' : date,
            'createdBy' : createdBy,
            'type': record_type,
            'location' : location,
            'status' : status,
            'comment' : comment
        }
        self.data.append(details)
        return self.data


    def delete_record(self,id):
        """This method deletes a record given the id"""

        incident = [incident for incident in incidents
                   if incident["id"] == id]    
        incident.remove(incident[0])
        return incident  