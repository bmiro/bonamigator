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
        candidates = list(participants)

        for participant in participants:
            participant_was_in_candidate_list = participant in candidates

            if participant_was_in_candidate_list:
                candidates.remove(participant)

            excluded_candidates = []
            if participant in excludes: # Participant has excludes (no is excluded!)
                for exclude in excludes[participant]:
                    if exclude in candidates:
                        candidates.remove(exclude)
                        excluded_candidates.append(exclude)

            if candidates == []:
                # participant was the only one in the list. Fuck!
                retry = True
                break

            bonamic = rand_choice(candidates)
            bonamics[participant] = bonamic

            candidates.remove(bonamic)

            if participant_was_in_candidate_list:
                candidates.append(participant)

            candidates.extend(excluded_candidates)

    return bonamics
