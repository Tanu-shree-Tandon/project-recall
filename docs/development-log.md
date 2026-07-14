# Project Recall Development Log

---

## Day 1

### Objective

Establish the project foundation and development workflow.

### Completed

- Created the GitHub repository.
- Initialized Git and connected the local repository to GitHub.
- Learned the Git workflow (add, commit, push).
- Designed the initial project vision.
- Created and refined the project README.
- Planned the high-level architecture for the MVP.

### Key Decisions

- Project name: Project Recall.
- Backend will be developed using Python and FastAPI.
- Focus on delivering an MVP that solves context reconstruction for students and researchers.

### Lessons Learned

- Understood how Git tracks project history.
- Learned the importance of meaningful commit messages.
- Realized the value of planning before implementation.

### Reflection

Today was about laying the foundation. While no functional features were built yet, I established the repository structure, version control workflow, and a clear vision for the project. This setup will make future development more organized and maintainable.

### Next Steps

- Set up the backend environment.
- Learn FastAPI fundamentals.
- Build the first API endpoint.

# Project Recall Development Log

---

# Day 1 – Project Foundation

## Objective

Establish the project foundation and development workflow.

## Completed

- Created the GitHub repository.
- Initialized Git and connected the local repository to GitHub.
- Learned the Git workflow (add, commit, push).
- Created and refined the project README.
- Defined the initial project vision and MVP scope.

## Key Decisions

- Project name: Project Recall.
- Python chosen as the primary language.
- FastAPI selected as the backend framework.
- Project positioned as an AI-powered context reconstruction assistant rather than a generic document chatbot.

## Lessons Learned

- Basic Git workflow.
- Importance of meaningful commit messages.
- Importance of planning before implementation.

## Reflection

Today focused on building the project's foundation. Although no functional features were implemented, the repository, documentation, and workflow are now ready for development.

## Next Steps

- Set up the backend.
- Learn FastAPI fundamentals.
- Build the first API endpoint.

---

# Day 2 – Backend Foundation

## Objective

Set up the backend environment and understand the fundamentals of FastAPI.

## Completed

- Created the `backend` directory.
- Created and activated a Python virtual environment.
- Learned why virtual environments are essential.
- Installed FastAPI.
- Installed Uvicorn.
- Learned how `pip` manages project dependencies.
- Explored installed package information using `pip show`.
- Created the first FastAPI application.
- Created the first GET endpoint (`/`).
- Successfully started the backend server using Uvicorn.
- Accessed the backend from the browser.
- Explored FastAPI's automatically generated API documentation (`/docs`).

## Key Decisions

- Keep the backend isolated using a project-specific virtual environment.
- Learn every concept before moving to the next feature rather than copying tutorials.
- Build the project incrementally with a production-oriented mindset.

## Concepts Learned

- Virtual environments
- Python packages
- Dependencies
- FastAPI applications
- API endpoints
- Routes
- Request-response lifecycle
- Automatic API documentation
- Running a development server with Uvicorn

## Reflection

Today was the first day the project became a working application. While some concepts—especially `app = FastAPI()`—required deeper understanding, I now understand the overall request-response flow and how a FastAPI application serves requests. Seeing the backend respond through the browser made the project feel real for the first time.

## Next Steps

- Learn additional routing concepts.
- Understand different HTTP methods.
- Begin handling user input.
- Start implementing file upload functionality.