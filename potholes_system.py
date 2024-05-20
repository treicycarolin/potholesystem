# Define actors and use cases
actors = ["Citizen", "Public Works Department", "Repair Crew", "Admin"]
use_cases = [
    {
        "actor": "Citizen",
        "use_cases": [
            "Log in",
            "Report Pothole",
            "Track Pothole",
            "Report Damage"
        ]
    },
    {
        "actor": "Public Works Department",
        "use_cases": [
            "Identify Pothole",
            "Log repair request",
            "View Pothole Reports",
        ]
    },
    {
        "actor": "Repair Crew",
        "use_cases": [
            "Update Status"
        ]
    },
    {
        "actor": "Admin",
        "use_cases": [
            "Generate Reports",
            "Manage System"
        ]
    }
]

# Print out the actors and use cases
print("Actors and their use cases for PHTRS:\n")
for actor in actors:
    print(f"Actor: {actor}")
    for item in use_cases:
        if item["actor"] == actor:
            for use_case in item["use_cases"]:
                print(f"  - Use Case: {use_case}")
    print()

# Brief description of the UML use case diagram
description = """
The UML use case diagram for the Pothole Tracking and Repair System (PHTRS) includes the following actors:
1. Citizen: They can report the potholes, track the status, and report any damages caused by potholes.
2. Public Works Department: Is responsible for viewing reports of potholes that need attention.
3. Repair Crew: Updates the system with the status of the repair work being done on the potholes.
4. Administrator: Manages the overall system, including user accounts, and generates necessary reports for analysis.

Each actor engages with the system through distinct use cases that outline their responsibilities and activities within the PHTRS. Citizens use the system to report and monitor potholes, as well as to report damages. Public Works Department are responsible for logging repair request and reviewing reports. The Repair Crew updates the progress of repairs. The Administrator oversees the system's management and produces reports for performance and operational analysis.
"""

print(description)
