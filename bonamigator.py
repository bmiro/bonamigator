#!/usr/bin/env python


from random import choice as rand_choice

def bon_amic(participants, excludes=None):
    """ @return a dictionary of bons amics giving a list of participants
    " and an optional dictionary of excludes.
    "
    " participants example:
    " [
    "  "jaumemateumateu", "bartomeumiromateu", "guillemmiromateu",
    "  "joanmateuparra"
    " ]
    "
    " exlcudes example:
    " {
    "   "jaumemateumateu" : ["joanmateuparra", "bartomeumiromateu"],
    "   "joanmateuparra": ["jaumemateumateu"]
    " }
    " 
    " @return example:
    " {
    "   "jaumemateumateu": "guillemmiromateu",
    "   "guillemmiromateu": "joanmateuparra",
    "   "joanmateuparra": "bartomeumiromateu",
    "   "bartomeumiromateu": "jaumemateumateu",
    " }
    "
    """

    if excludes == None:
        excludes = []

    retry = True
    while retry:
        retry = False

        bonamics = {}
        remaining_participants = list(participants)

        for participant in participants:
            participant_was_in_list = participant in remaining_participants

            if participant_was_in_list:
                remaining_participants.remove(participant)

            if remaining_participants == []:
                # participant was the only one in the list. Fuck!
                retry = True
                break

            bonamic = rand_choice(remaining_participants)
            bonamics[participant] = bonamic

            remaining_participants.remove(bonamic)

            if participant_was_in_list:
                remaining_participants.append(participant)

    return bonamics
