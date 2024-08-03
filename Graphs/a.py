import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

# Define the WBS hierarchy
wbs = {
    '1': {'label': '1. Project Management', 'children': {
        '1.1': {'label': '1.1 Project Planning', 'children': {
            '1.1.1': '1.1.1 Define Project Scope (Gaganjot)',
            '1.1.2': '1.1.2 Develop Project Plan (Harshil)',
        }},
        '1.2': {'label': '1.2 Team Management', 'children': {
            '1.2.1': '1.2.1 Assign Roles and Responsibilities (Dhruv)',
            '1.2.2': '1.2.2 Conduct Team Meetings (Rutraj)',
        }},
        '1.3': {'label': '1.3 Schedule Management', 'children': {
            '1.3.1': '1.3.1 Develop Project Schedule (Sooyeon)',
            '1.3.2': '1.3.2 Monitor Project Progress (Gaganjot)',
        }},
        '1.4': {'label': '1.4 Risk Management', 'children': {
            '1.4.1': '1.4.1 Identify Risks (Harshil)',
            '1.4.2': '1.4.2 Develop Risk Mitigation Plan (Dhruv)',
        }},
        '1.5': {'label': '1.5 Quality Management', 'children': {
            '1.5.1': '1.5.1 Define Quality Standards (Rutraj)',
            '1.5.2': '1.5.2 Conduct Quality Reviews (Sooyeon)',
        }},
        '1.6': {'label': '1.6 Communication Management', 'children': {
            '1.6.1': '1.6.1 Develop Communication Plan (Gaganjot)',
            '1.6.2': '1.6.2 Manage Stakeholder Communication (Harshil)',
        }},
    }},
    '2': {'label': '2. Requirements Analysis', 'children': {
        '2.1': {'label': '2.1 Functional Requirements Analysis', 'children': {
            '2.1.1': '2.1.1 Gather Functional Requirements (Dhruv)',
            '2.1.2': '2.1.2 Document Functional Requirements (Rutraj)',
        }},
        '2.2': {'label': '2.2 Non-Functional Requirements Analysis', 'children': {
            '2.2.1': '2.2.1 Gather Non-Functional Requirements (Sooyeon)',
            '2.2.2': '2.2.2 Document Non-Functional Requirements (Gaganjot)',
        }},
        '2.3': {'label': '2.3 Stakeholder Requirements Analysis', 'children': {
            '2.3.1': '2.3.1 Identify Stakeholders (Harshil)',
            '2.3.2': '2.3.2 Document Stakeholder Requirements (Dhruv)',
        }},
        '2.4': {'label': '2.4 Requirements Documentation', 'children': {
            '2.4.1': '2.4.1 Compile Requirements Specification (Rutraj)',
            '2.4.2': '2.4.2 Review and Approve Requirements Document (Sooyeon)',
        }},
    }},
    '3': {'label': '3. System Design', 'children': {
        '3.1': {'label': '3.1 Architectural Design', 'children': {
            '3.1.1': '3.1.1 Develop System Architecture (Gaganjot)',
            '3.1.2': '3.1.2 Review Architectural Design (Harshil)',
        }},
        '3.2': {'label': '3.2 Database Design', 'children': {
            '3.2.1': '3.2.1 Design Database Schema (Dhruv)',
            '3.2.2': '3.2.2 Implement Database Design (Rutraj)',
        }},
        '3.3': {'label': '3.3 UI/UX Design', 'children': {
            '3.3.1': '3.3.1 Develop UI Wireframes (Sooyeon)',
            '3.3.2': '3.3.2 Design User Experience Flow (Gaganjot)',
        }},
        '3.4': {'label': '3.4 Component Design', 'children': {
            '3.4.1': '3.4.1 Design System Components (Harshil)',
            '3.4.2': '3.4.2 Document Component Specifications (Dhruv)',
        }},
        '3.5': {'label': '3.5 Security Design', 'children': {
            '3.5.1': '3.5.1 Identify Security Requirements (Rutraj)',
            '3.5.2': '3.5.2 Develop Security Measures (Sooyeon)',
        }},
    }},
    '4': {'label': '4. Development', 'children': {
        '4.1': {'label': '4.1 Frontend Development', 'children': {
            '4.1.1': '4.1.1 Home Page Development (Harshil)',
            '4.1.2': '4.1.2 Sign Up Page Development (Sooyeon)',
            '4.1.3': '4.1.3 Sign In Page Development (Dhruv)',
            '4.1.4': '4.1.4 Product Details Page Development (Rutraj)',
            '4.1.5': '4.1.5 Cart Page Development (Gaganjot)',
            '4.1.6': '4.1.6 Filter Vehicle Page Development (Harshil)',
            '4.1.7': '4.1.7 Second-Hand Listing Page Development (Sooyeon)',
            '4.1.8': '4.1.8 Contact Us Page Development (Dhruv)',
            '4.1.9': '4.1.9 Add Product Page Development (Rutraj)',
            '4.1.10': '4.1.10 Open Store Page Development (Gaganjot)',
            '4.1.11': '4.1.11 About Us Page Development (Harshil)',
            '4.1.12': '4.1.12 Dashboard Development (Sooyeon)',
        }},
        '4.2': {'label': '4.2 Backend Development', 'children': {
            '4.2.1': '4.2.1 User Management System (Dhruv)',
            '4.2.2': '4.2.2 Product Catalog Management (Rutraj)',
            '4.2.3': '4.2.3 Search and Filtering System (Gaganjot)',
            '4.2.4': '4.2.4 Shopping Cart and Checkout System (Harshil)',
            '4.2.5': '4.2.5 Order Management System (Sooyeon)',
            '4.2.6': '4.2.6 Warehouse Management System (Dhruv)',
            '4.2.7': '4.2.7 Analytics and Reporting Tools (Rutraj)',
            '4.2.8': '4.2.8 Security Implementation (Gaganjot)',
        }},
    }},
    '5': {'label': '5. Testing', 'children': {
        '5.1': {'label': '5.1 Unit Testing', 'children': {
            '5.1.1': '5.1.1 Develop Test Cases (Sooyeon)',
            '5.1.2': '5.1.2 Execute Unit Tests (Gaganjot)',
        }},
        '5.2': {'label': '5.2 Integration Testing', 'children': {
            '5.2.1': '5.2.1 Develop Integration Test Plan (Harshil)',
            '5.2.2': '5.2.2 Execute Integration Tests (Dhruv)',
        }},
        '5.3': {'label': '5.3 System Testing', 'children': {
            '5.3.1': '5.3.1 Develop System Test Plan (Rutraj)',
            '5.3.2': '5.3.2 Execute System Tests (Sooyeon)',
        }},
        '5.4': {'label': '5.4 User Acceptance Testing', 'children': {
            '5.4.1': '5.4.1 Develop UAT Plan (Gaganjot)',
            '5.4.2': '5.4.2 Conduct UAT (Harshil)',
        }},
        '5.5': {'label': '5.5 Performance Testing', 'children': {
            '5.5.1': '5.5.1 Develop Performance Test Plan (Dhruv)',
            '5.5.2': '5.5.2 Execute Performance Tests (Rutraj)',
        }},
    }},
    '6': {'label': '6. Deployment', 'children': {
        '6.1': {'label': '6.1 Infrastructure Setup', 'children': {
            '6.1.1': '6.1.1 Provision Servers (Sooyeon)',
            '6.1.2': '6.1.2 Configure Servers (Gaganjot)',
        }},
        '6.2': {'label': '6.2 Application Deployment', 'children': {
            '6.2.1': '6.2.1 Deploy Application (Harshil)',
            '6.2.2': '6.2.2 Verify Deployment (Dhruv)',
        }},
        '6.3': {'label': '6.3 Data Migration', 'children': {
            '6.3.1': '6.3.1 Plan Data Migration (Rutraj)',
            '6.3.2': '6.3.2 Execute Data Migration (Sooyeon)',
        }},
        '6.4': {'label': '6.4 Go-Live', 'children': {
            '6.4.1': '6.4.1 Conduct Final System Checks (Gaganjot)',
            '6.4.2': '6.4.2 Go-Live (Harshil)',
        }},
    }},
    '7': {'label': '7. Maintenance and Support', 'children': {
        '7.1': {'label': '7.1 Maintenance', 'children': {
            '7.1.1': '7.1.1 Monitor System (Dhruv)',
            '7.1.2': '7.1.2 Perform Regular Maintenance (Rutraj)',
        }},
        '7.2': {'label': '7.2 Support', 'children': {
            '7.2.1': '7.2.1 Provide User Support (Sooyeon)',
            '7.2.2': '7.2.2 Address Issues and Bugs (Gaganjot)',
        }},
    }},
}

def add_nodes_edges(graph, data, parent=None):
    for key, value in data.items():
        graph.add_node(key, label=value['label'] if isinstance(value, dict) else value)
        if parent:
            graph.add_edge(parent, key)
        if isinstance(value, dict) and 'children' in value:
            add_nodes_edges(graph, value['children'], key)

# Create a directed graph
G = nx.DiGraph()
add_nodes_edges(G, wbs)

# Define position using graphviz layout for hierarchical structure
pos = graphviz_layout(G, prog='dot')

# Draw the graph
plt.figure(figsize=(15, 15))
nx.draw(G, pos, with_labels=True, labels=nx.get_node_attributes(G, 'label'), node_size=3000, node_color='lightblue', font_size=8, font_weight='bold', arrows=True)
plt.title('Work Breakdown Structure')
plt.show()
