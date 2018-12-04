from datetime import datetime

incidents = []

class IncidentModel():

    def __init__(self):
        self.data = incidents


    def get_all_records(self):
        """This method fetches all records"""
        return self.data

    def get_single_record(self,id):
        """This method fetches a single record given the id"""

        incident = [incident for incident in incidents
                   if incident["id"] == id]
        return incident


    def save(self,createdBy,record_type,location,comment ):
        """This method to create and save a dict object"""
        
        status = 'Draft'
        date = datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
        details = {
            'id' : len(self.data)+1,
            'createdOn' : date,
            'createdBy' : createdBy,
            'type': record_type,
            'location' : location,
            'status' : status,
            'comment' : comment
        }
        self.data.append(details)
        return self.data


    def update_comment(self, comment, index):
        """This method updates comment record"""

        data = comment

        for comment in incidents:
            incidents[index]['comment'] = data
            # return incidents list

    def update_location(self, location, index):
        """This method Edits existing location record"""

        data = location

        for location in incidents:
            incidents[index]['location'] = data

    def get_index(self,id):
        """This method gets index position of a record"""
        
        index = 0
        for incident in incidents:
            if incident["id"] == id:
                return index
            index += 1
        return index