# ECCCH Technical Glossary

This glossary provides definitions of technical terms used across the ECCCH platform and its engineering documentation, covering architecture, access, knowledge and data, integration, infrastructure and operations.

**Jump to:** [Architecture](#architecture-services) · [Access](#access-platform) · [Knowledge & storage](#knowledge-data-storage) · [Semantics](#data-semantic-technologies) · [Execution](#execution-applications) · [Integration](#interfaces-integration) · [Hosting](#hosting-resources) · [Delivery](#delivery-configuration) · [Operations](#monitoring-continuity)

## Architecture, services and responsibilities {#architecture-services}

| Term | Definition |
| --- | --- |
| Cloud component | A building block of the ECCCH architecture with a defined responsibility, such as managing storage, coordinating processing or providing access to knowledge. That responsibility may be implemented by one software service or several services working together. |
| Low-level cloud component | A technical building block supporting the infrastructure on which applications and platform services run. Examples include container scheduling, networking, storage provisioning and infrastructure monitoring. These functions may be supplied by an existing hosting platform or implemented specifically for ECCCH where required. |
| Capability | A function that a user or integrating application can use, such as shared sign-in, file upload or processing. A capability may depend on several cloud components working together. |
| Software implementation | The software used to fulfil an architectural responsibility, including its code, dependencies and configuration. An implementation name does not necessarily identify an additional architectural component. |
| Service | A software function made available to users or other systems through a defined interface. A service may provide a user interface, an API or both. |
| Infrastructure as a Service (IaaS) | Computing infrastructure provided as a service, including virtual machines, networking and storage. The infrastructure operator maintains the underlying environment. The customer normally maintains the operating system and software installed on its virtual machines. |
| Platform as a Service (PaaS) | A managed environment for deploying and running applications. The platform operator maintains the shared infrastructure and runtime. Application teams maintain their software, deployment configuration and service-specific controls. |
| Software as a Service (SaaS) | Software provided as a hosted service. Users access its functions through a browser or another supported interface without installing or maintaining the underlying application. |
| Architectural layer | A group of components with related responsibilities. For example, an access layer handles entry to services, while an execution layer runs processing tasks. Layers do not necessarily correspond to separate servers or deployments. |
| Control plane | The part of the platform that manages and coordinates requests. It handles functions such as resource registration, operation tracking and the selection of appropriate services or storage destinations. |
| Execution plane | The part of the platform that performs requested work, such as running tools, transforming data or transferring files. It uses assigned resources and reports progress and results. |
| Hosting | Providing the computing environment in which software runs. Hosting includes resources such as servers, virtual machines, container platforms, networking and storage. |
| Deployment | Installing and configuring a particular software version in a hosting environment so that it can run. An application may have separate deployments for development, staging and production. |
| Hosting Entity | The organisation responsible for providing and operating the agreed ECCCH hosting environment. Its infrastructure responsibilities are separate from the responsibility for maintaining each deployed application or component. |
| Hosting provider | An organisation supplying infrastructure or a managed platform on which software runs. Another organisation may maintain the software deployed there. |
| Service provider | The organisation or team responsible for delivering and maintaining a service. It may use its own infrastructure or infrastructure supplied by a hosting provider. |
| ECCCH-hosted / ECCCH-managed | The service runs in the hosting environment arranged for ECCCH and is maintained by the responsible ECCCH service team. The hosting operator and software maintenance team may be different organisations. |
| ECCCH-hosted / Provider-managed | The service runs in the hosting environment arranged for ECCCH, while its provider maintains the application and its configuration. The hosting operator maintains the underlying infrastructure or platform. |
| Provider-hosted / Provider-managed | The provider arranges the service's hosting and maintains the service. It can connect to ECCCH through agreed interfaces while remaining outside central ECCCH hosting. |
| Provider-hosted / ECCCH-managed | The service runs on infrastructure supplied outside central ECCCH hosting, while an ECCCH team maintains the service under an agreed operational arrangement. |
| Self-hosted / Self-managed | From an integrating organisation's perspective, deploying and maintaining its own instance of software. It may run that instance on its own infrastructure or on a platform supplied by another organisation. |
| Federation | Connecting independently operated services, repositories or execution environments through agreed interfaces. Access and trust arrangements depend on the participating systems and the type of integration. Connected organisations retain responsibility for their own resources. |

## Access and platform coordination {#access-platform}

| Term | Definition |
| --- | --- |
| Cloud Web UI / Portal (ECCCH cloud component) | The main browser interface for accessing ECCCH services. It helps users find resources, access workspaces and start supported actions. It presents functions delivered by other components, such as knowledge management, storage and processing. |
| Single Entry Point (SEP) (shared ECCCH access capability) | The shared access capability through which users and applications reach ECCCH services. It is supported by the Portal, API Gateway, AAI and platform integration interfaces. It is broader than any one component and does not require every request to pass through a single application. |
| Access Edge / API Gateway (ECCCH cloud component) | The technical entry point for platform APIs. Its architectural responsibilities include routing, transport protection, token validation and route-level access controls. Receiving services enforce permissions specific to their resources and operations. Apache APISIX is used to implement the gateway role. |
| Authentication and Authorisation Infrastructure (AAI) (ECCCH cloud component) | The services and trust arrangements used to identify users and applications and supply information relevant to access decisions. Connected services combine this information with their own permissions. Shared sign-in does not automatically grant access to every resource. |
| EGI Check-in (external AAI service) | A federated identity service connecting accepted identity providers to research services. It enables supported sign-in methods and supplies identity information to connected applications. Each application configures how that information affects access. |
| Authentication | Establishing the identity of a user, application or service. For example, authentication determines which account is making a request. |
| Authorisation | Deciding whether a user or application may perform a particular action on a resource. For example, a user may be permitted to read a dataset but not edit or publish it. |
| Role / Group / Entitlement | Information that can support access decisions. A role describes a responsibility, such as workspace administrator. A group identifies a set of users. An entitlement expresses a recognised access-related attribute or right. Services define how these values affect permissions. |
| Access token | A credential presented to access a protected API. The relevant gateway or service validates it and applies the applicable access rules. A valid token does not automatically authorise every operation. |
| OpenID Connect (OIDC) | A standard supporting user sign-in and the communication of identity information to applications. It builds on OAuth 2.0. |
| OAuth 2.0 | A framework through which applications obtain limited access to protected services using access tokens. The permitted access depends on the granted permissions and the receiving service's rules. |
| SEP Integration API / Common Platform API (ECCCH cloud component) | The integration interface through which authorised applications request selected shared ECCCH functions. It connects supported requests to the responsible platform services. Common Platform API is the implementation name used in MS17, distinguishing this interface from the complete SEP capability. |
| Platform Core (implementation name) | The deployment name for the backend hosting the Common Platform API and Portal Backend for Frontend. These interfaces currently share a codebase and deployment. Platform Core is an implementation name rather than an additional architectural component. |
| Backend for Frontend (BFF) | A backend interface designed for a particular user interface. It prepares the information and operations that the interface needs and may combine responses from several services. The Portal BFF serves this purpose for the ECCCH Portal. |
| Access / Entitlement Mapper (AEM) (ECCCH cloud component) | Resolves the access and operation context for platform-facing requests using trusted identity information and applicable semantic, storage and workspace policy inputs. It does not own those authoritative records or replace the access checks performed by domain services. AEM is not required to act as the central decision point for every request. |
| Resource Manager (ECCCH cloud component) | The component that registers resources such as applications, datasets, tools and workflows, and maintains information needed to discover and use them. It supports visibility and registration status. Its role differs from allocating CPU or memory to workloads. |
| Processing Manager (ECCCH cloud component) | Coordinates and records the progress of managed operations, including selected cross-component lifecycle and execution flows. Execution workers and other services perform the domain-specific work. The Processing Manager tracks the operation state without becoming the owner of semantic content or binary storage. |
| Managed operation | A platform-governed action with a durable identifier and recorded state, used when a lifecycle or execution flow crosses component boundaries or needs coordinated completion. Examples may include save, publish or selected processing flows. Ordinary local CRUD requests do not automatically become managed operations. |
| Context resolution | Determining the information needed to carry out a request, such as the relevant user, workspace, permissions, resource identifiers and storage destination. This provides the responsible services with the context required for the operation. |

## Knowledge, data and storage components {#knowledge-data-storage}

| Term | Definition                                                                                                                                                                                                                                                                                                                                                                      |
| --- |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Heritage Digital Twin (HDT) | In HDTO v1.1, an HC2 Heritage Digital Twin aggregates sets of formal propositions about an HC1 Heritage Entity, organised as HC16 Heritage Proposition Sets. Its content may include links to digital representations and supporting documentation, and can change through Digital Twin Maintenance actions. An HDT is not the heritage entity itself or a single digital file. |
| Heritage Digital Twin Ontology (HDTO) | The CIDOC CRM-based ECHOES ontology described in D7.1 for representing Heritage Entities (HC1), Heritage Digital Twins (HC2), Heritage Proposition Sets (HC16) and their relationships, including changes to HDT content. HDTO v1.1 specifies the corresponding classes and properties.                                                                                         |
| Knowledge Base (KB) (semantic repository managed through ECCCH knowledge services) | The semantic content made available through ECCCH knowledge services and its underlying repositories. It includes machine-readable descriptions of heritage entities and their relationships, including HDT-related information. The content may be distributed across connected repositories.                                                                                  |
| Knowledge Base API / Knowledge API (interface to knowledge services) | An interface through which applications access knowledge services. Supported functions can include querying registered semantic repositories and retrieving information. Its responsibilities differ from the broader platform functions exposed through the Common Platform API.                                                                                               |
| Knowledge Base Management System (KBMS) (ECCCH cloud component) | The services that provide governed access to and management of the Knowledge Base, including supported semantic queries, graph and workspace operations, enrichment and publication. KBMS manages semantic state and access within its domain.                                                                                                                                  |
| Knowledge Graph (KG) | A semantic network representation of domain knowledge, consisting of entities (nodes) and their interrelationships (edges), typically modeled using standards like RDF (Resource Description Framework) and OWL (Web Ontology Language). It represents information in a machine-readable format that captures context and meaning.                                              |
| Knowledge Services | Platform functions for accessing, querying, managing, enriching and publishing semantic information. In ECCCH these functions are mainly exposed through KBMS and its interfaces and operate on supported semantic repositories.                                                                                                                                                |
| Administrative Repository (ECCCH cloud component) | The authoritative store for semantic governance metadata, including ownership, graph and node assignments, workspace definitions and related registration or publication information. It provides governance information used by KBMS and other platform services, rather than serving as the RDF content repository itself.                                                    |
| Storage Manager (ECCCH cloud component) | The file-handling role called Non-Semantic Data & Integration Manager in D6.3. It manages binary upload sessions, transfer or routing to approved storage destinations, stable asset references and relevant storage-side lifecycle transitions. Storage target definitions, availability and policy state are governed separately by the Storage Registry / Data API.          |
| Storage Registry / Data API (ECCCH cloud component) | The authoritative register of storage targets, including their technical configuration, availability, policy state, usage and quota information. Platform services use these records to resolve permitted storage destinations. The registry and the file-handling manager have distinct architectural responsibilities, even when implemented together.                        |
| User Personal Space (UPS) (shared ECCCH workspace capability) | A user's private working context for preparing heritage information and associated files before sharing or publication. It combines semantic information and binary assets through the relevant services. It does not necessarily correspond to one dedicated folder, database or storage bucket.                                                                               |
| Workspace | A working context grouping related resources, members and permissions. It may support individual preparation or collaboration. Its information and files can be held across several knowledge and storage services.                                                                                                                                                             |

## Data and semantic technologies {#data-semantic-technologies}

| Term | Definition |
| --- | --- |
| Dataset | An identifiable collection of related data managed as a unit. It may contain structured records, files or a combination of both. Its description should explain its content, structure and conditions of use. |
| Metadata | Structured information describing a resource, such as its title, creator, format, date, licence or location. Systems use metadata to help identify, discover, manage and reuse resources. |
| Paradata | Information about the methods, decisions and circumstances involved in creating or interpreting digital material. For example, it can explain which assumptions and processing methods were used to produce a digital reconstruction. |
| Binary asset | A file managed as digital content, such as an image, PDF, audio recording or 3D model. Its content is held in file or object storage, while semantic records may refer to it through identifiers. |
| Resource identifier | A value identifying a resource, such as a dataset, HDT, file or operation. It allows systems to reference the resource without relying only on its displayed name. |
| Persistent identifier (PID) | An identifier managed to remain usable over time, including when a resource's location changes. Its persistence depends on the technical and organisational arrangements maintaining it. |
| Semantic data | Data expressed using identified concepts and relationships so that software can interpret connections between entities. For example, a description can explicitly link a heritage object to its creator, production event and place of origin. |
| Ontology | A formal description of concepts and their relationships. It provides a shared structure for representing information, such as the relationship between an object, an event and a person. |
| Controlled vocabulary | An agreed set of terms and identifiers used to describe information consistently. It may include preferred labels, alternative labels and relationships between terms. |
| Semantic artefact | A reusable resource defining or organising meaning, such as an ontology, thesaurus, controlled vocabulary or mapping. Applications use these resources to interpret and exchange information consistently. |
| CIDOC Conceptual Reference Model (CIDOC CRM) | A reference ontology for describing cultural heritage information and connecting descriptions from different sources. It defines concepts for entities, events and relationships that can support more specialised models. |
| Resource Description Framework (RDF) | A standard for expressing information as statements linking entities, properties and values. These statements form graphs that software can store, query and connect. |
| RDF triple | One RDF statement consisting of a subject, predicate and object. For example, it can state that a particular object has a particular creator. |
| Named graph | An identified collection of RDF statements within a repository. It can organise information by source, workspace or another agreed boundary. Access protection depends on the services managing it. |
| Semantic repository / Triplestore | A database designed to store and query RDF graphs. It provides storage and query functions used by knowledge services. A repository is one part of a KBMS rather than the complete management system. |
| SPARQL | A standard language for querying and updating RDF data. Applications use it to retrieve information matching specified entities, properties and relationships. |
| SPARQL endpoint | A network interface accepting SPARQL requests. It exposes the supported query or update functions of a repository or knowledge service. |
| Federated semantic query | A query operation accessing information from several semantic repositories. Implementations may collect separate results or combine information more extensively. Querying multiple endpoints does not by itself demonstrate joins across repositories. |
| Data mapping | Defining how information in one structure or vocabulary corresponds to another. For example, mapping can connect fields in a source catalogue to concepts in the ECCCH data model. |
| Data ingestion / Bulk ingestion | Bringing data into a managed system and applying the required processing. Bulk ingestion handles many records or files together and may require batching, validation, progress tracking and error reporting. |
| Data validation | Checking data against stated rules, such as required properties, permitted values or valid formats. Structural validation does not establish the historical accuracy of every statement. |
| Shapes Constraint Language (SHACL) | A standard for expressing and checking rules for RDF data. It can specify requirements such as which properties must be present and which kinds of values they may contain. |
| Provenance / Data lineage | Information recording where data came from and how it was produced or changed. It can connect a result to source records, processing steps, software versions and responsible agents. |
| Version / Revision | An identified state of software or data. Its identifier allows users and systems to refer to the state they used. Retaining an identifier does not automatically mean that all earlier content remains retrievable. |
| Storage target | A registered destination where files can be stored. Its selection depends on the applicable access rules, storage policies and technical requirements. |
| Object storage | Storage that manages content as individually addressable objects accessed through an API. Each object can include content and associated metadata. |
| S3-compatible API | An interface supporting commonly used Amazon S3-style operations for object storage. It can be provided by systems operated outside Amazon. |
| Block storage | Storage presented as a disk-like volume. It is commonly used by databases and other applications requiring persistent filesystem access. |
| Shared file storage | A filesystem accessible by several authorised workloads. Its sharing and access capabilities depend on the storage configuration. |

## Execution components and applications {#execution-applications}

| Term | Definition |
| --- | --- |
| Workflow orchestration substrate (ECCCH cloud component) | The technical foundation for coordinating multi-step or long-running work. It records progress and dependencies so tasks run in the appropriate order and can resume or retry after interruptions where supported. |
| Queue and workload manager (ECCCH cloud component) | The component controlling when submitted work can run and which processing resources it may use. It can apply priorities, capacity limits and scheduling rules. A messaging service alone does not provide the complete workload management role. |
| Execution workers and runtime services (ECCCH cloud component) | The processes and environments that perform requested work, such as OCR, data transformation, AI inference or file transfer. They use assigned resources and report status and results to the coordinating services. |
| Tool Catalogue / Toolbox (ECCCH cloud component) | The component recording the information needed to run supported tools, including their inputs, outputs, invocation interfaces and runtime requirements. It supports processing services and has a more specific execution role than a general resource discovery catalogue. |
| AI-enabled execution (optional ECCCH cloud capability) | Processing functions using AI models for tasks such as recognition, classification or analysis. They use the applicable access, tool registration and processing arrangements. Their hardware requirements depend on the model and task. |
| Application | Software supporting a user or organisational task through a user interface, an API or both. An application may use shared ECCCH functions while retaining its own backend and data management. |
| Vertical Application (VA) | An application supporting a particular heritage activity or specialist workflow. It can integrate with ECCCH capabilities such as sign-in, knowledge access, storage and processing while remaining a separately maintained application. |
| Tool | Software performing a focused task, such as recognising text, converting a file or validating data. A tool may run independently, be embedded in an interface or form a step in a workflow. |
| Domain API / Lightweight tool | A specialised interface or small software service providing a focused function for applications or users. It can support ECCCH workflows without implementing the broader responsibilities of a shared platform component. |
| VA adapter / Application-side connector (integration software) | Software connecting an application's interfaces and data structures to the ECCCH functions it needs. It can translate requests, identifiers, formats or responses. Depending on the integration, it may be a separate component or a set of endpoints within an existing service. |
| External provider or repository | A service or data source maintained outside central ECCCH hosting and connected through an agreed interface. Its provider retains responsibility for its operation and applicable access conditions. |

## Interfaces and integration {#interfaces-integration}

| Term | Definition |
| --- | --- |
| Application Programming Interface (API) | A defined way for software systems to request functions or exchange information. Its documentation explains the supported operations, required inputs, responses and access conditions. |
| API endpoint | A particular operation exposed at an API address. For example, one endpoint may accept an upload request while another returns processing status. |
| REST API | An API following a resource-oriented interaction style, commonly using HTTP methods and addresses. Its contract defines the behaviour of each supported operation. |
| API contract / OpenAPI specification | An API contract defines how clients and services communicate. An OpenAPI specification expresses an HTTP API contract in a machine-readable form, describing operations, parameters, requests and responses. |
| JSON / JSON-LD | JSON is a format for exchanging structured data. JSON-LD adds links between data fields and identified concepts, allowing the information to be interpreted as linked data. |
| Integration | Connecting an application, dataset, tool or service to the ECCCH functions it needs. This includes configuring interfaces, identity handling, data formats and the treatment of results and errors. |
| Interoperability | The ability of systems to exchange information and use it correctly through compatible interfaces, formats and agreed meanings. A successful network connection alone does not establish interoperability. |
| Integration route | The technical way a system connects to ECCCH, such as calling the Common Platform API, using a component's own API or connecting through an adapter. The appropriate route depends on the required function and supported interfaces. |
| Integration level / Interoperability level | Separate classifications used for different purposes. Integration levels describe participation in the integration model. D6.2 interoperability levels describe conformance with applicable interoperability requirements. The classifications should not be treated as equivalent. |
| Conformance | Meeting a specified set of technical requirements, such as an API contract or data validation rules. The requirements and checks must be identified to make a conformance claim meaningful. |
| Idempotency | A property allowing a request to be repeated without unintentionally creating additional effects. For example, retrying an idempotent creation request should not create a duplicate resource. |
| Asynchronous operation | An operation continuing after the initial request has been acknowledged. The client obtains progress or results later through a supported mechanism, such as a status endpoint or notification. |
| Workflow | A defined sequence or network of processing steps, including dependencies and the handling of inputs and outputs. A workflow may involve several tools and services. |
| Event / Message broker | An event reports that something has happened, such as completion of an upload. A message broker transports messages between services, allowing them to communicate without requiring a continuous direct connection. |

## Hosting, runtime and resource allocation {#hosting-resources}

| Term | Definition |
| --- | --- |
| Container / Container image | A container runs software in an isolated environment using the host's operating system kernel. A container image packages the software and dependencies used to create that environment. |
| Container registry | A service storing and distributing container images. Deployment systems retrieve the selected image version when starting or updating a workload. |
| Kubernetes | A system for deploying and managing containerised workloads across a group of machines. It handles functions such as workload placement, restarts, networking and resource requirements. |
| OpenShift / OKD | Related Kubernetes-based platforms adding application deployment, access management and operational facilities. OKD is the community distribution used by the PCSS PaaS described in the deployment documentation. |
| OpenStack | A platform providing infrastructure services, including virtual machines, networks and storage. It supports workloads that require VM-based hosting rather than deployment on a container platform. |
| Virtual machine (VM) | A virtual computer with its own operating system and assigned resources. Several VMs can run on the same physical server while remaining separate environments. |
| Cluster / Node | A cluster is a group of machines managed as one computing environment. In Kubernetes, a node is a machine on which workloads can run. A node may be a physical server or a virtual machine. |
| Kubernetes namespace / OpenShift project | A logical area grouping workloads and related resources within a cluster. Access rules and quotas can be applied to it. An OpenShift project builds on a Kubernetes namespace and does not imply dedicated physical hardware. |
| Pod / Pod readiness | A Pod is the smallest deployable workload unit in Kubernetes and runs one or more containers together. Readiness indicates whether it passes configured checks and can receive service traffic. Functional behaviour requires separate testing. |
| Kubernetes Deployment / Replica | A Deployment is a controller maintaining the desired set of application Pods and managing their updates. A replica is one instance of the workload. Multiple replicas improve resilience only when the application and its dependencies support that arrangement. |
| StatefulSet | A Kubernetes controller providing stable workload identities and persistent storage associations. It is commonly used for stateful services but does not automatically configure database replication or recovery. |
| Kubernetes Service / Ingress / Route | A Service provides a stable network destination for selected Pods. An Ingress or OpenShift Route exposes configured HTTP services to clients outside the cluster. These resources differ from the broader meaning of a software service. |
| Resource request / Resource limit | A request declares CPU or memory requirements used for scheduling. A limit sets an enforced ceiling. CPU consumption may be throttled, while exceeding a memory limit can cause a container to be terminated. |
| ResourceQuota | A namespace-level rule limiting resources that workloads may request or allocate, such as CPU, memory, storage or object counts. A quota does not itself reserve dedicated hardware. |
| PersistentVolumeClaim (PVC) | A Kubernetes request for persistent storage. Once bound to a volume, it provides storage that can outlast an individual Pod. Allocated capacity and the quantity of stored data are separate measurements. |
| StorageClass | A Kubernetes definition describing how storage volumes are provisioned and which features they support, such as access arrangements and volume expansion. |
| CPU / Memory / GPU | CPU provides general-purpose processing. Memory holds information actively used by running software. A GPU performs many calculations in parallel and can accelerate suitable AI, imaging and scientific workloads. |
| Multi-Instance GPU (MIG) | A feature of supported NVIDIA GPUs dividing one physical GPU into smaller instances with assigned computing and memory resources. Availability depends on the hardware and platform configuration. |
| Scalability / Autoscaling | Scalability is the ability to adjust service capacity as demand changes. Autoscaling makes selected adjustments automatically using configured rules and measurements. Both depend on application design and available infrastructure. |
| Horizontal / Vertical scaling | Horizontal scaling adds workload instances. Vertical scaling changes resources assigned to an instance, such as CPU or memory. Different applications support these approaches to different degrees. |
| HorizontalPodAutoscaler (HPA) | A Kubernetes controller adjusting the number of workload replicas using configured metrics. It requires suitable settings, available capacity and an application supporting multiple instances. |

## Delivery and software configuration {#delivery-configuration}

| Term | Definition |
| --- | --- |
| Development / Staging / Production environment | Development supports implementation work. Staging supports testing before release under conditions intended to resemble production. Production delivers the operational service to its intended users. |
| Source code repository | A managed location storing software source code and its change history. It supports collaboration, review and the identification of the code used for a particular release. |
| Release | An identified software version made available for use. It should be associated with the relevant code, build artefacts, dependencies and deployment instructions. |
| Continuous Integration / Continuous Delivery (CI/CD) | Automated processes for building, checking, packaging and delivering software changes. Deployment may require approval or proceed automatically, depending on the configured workflow. |
| Deployment configuration | The settings describing how software should run in a target environment, including its image version, resources, network exposure, storage and dependencies. |
| Helm / Kustomize | Tools for managing Kubernetes deployment configuration. Helm packages applications with configurable settings. Kustomize adapts configuration for different environments. |
| GitOps / Argo CD | GitOps uses version-controlled configuration to describe the intended deployed state. Argo CD compares Kubernetes environments with that configuration and can apply the required changes. |
| Configuration secret | Sensitive configuration, such as a password, token or private key, supplied to software through a controlled mechanism. Its protection depends on storage, access and operational settings. |
| MkDocs | A tool for publishing documentation as a website from Markdown files. It supports a structured, version-controlled documentation source that teams can update alongside software development. |

## Monitoring and continuity {#monitoring-continuity}

| Term | Definition |
| --- | --- |
| Monitoring / Observability | Monitoring tracks selected health and performance signals. Observability uses information such as metrics, logs and traces to help operators understand system behaviour and investigate problems. |
| Metric / Log / Trace | A metric is a numerical measurement over time. A log records events or messages. A trace follows the steps of a request across services. Together, they help explain how a system behaves. |
| Health check / Alert | A health check tests a configured aspect of service behaviour. An alert notifies a responsible team when a specified condition occurs. Their effectiveness depends on what is checked and how responses are organised. |
| Observed utilisation | Measured use of resources such as CPU, memory or storage during a stated period. It differs from configured requests, limits and allocated capacity. |
| Latency / Throughput / Error rate | Latency measures how long an operation takes. Throughput measures work completed in a period. Error rate measures the proportion or frequency of unsuccessful operations. |
| High availability (HA) | A design intended to keep a service available during specified failures or maintenance activities. It requires suitable redundancy, failure handling and tested recovery across the service and its dependencies. |
| Pod anti-affinity | A Kubernetes placement rule keeping selected Pods apart across nodes or other defined locations. Its effectiveness depends on suitable capacity and scheduling configuration. |
| PodDisruptionBudget (PDB) | A Kubernetes rule limiting how many selected Pods may be unavailable during supported voluntary disruptions, such as node maintenance. It does not prevent every type of outage. |
| Replication / Failover | Replication maintains additional copies of data or service state. Failover transfers service to another suitable instance following a failure. Both require application-specific configuration. |
| Backup / Restore | A backup is a retained copy of data or configuration intended for recovery. Restore is the process of recovering from that copy. Successful backup execution and successful restoration are separate checks. |
| Disaster recovery | The arrangements for restoring services after a major disruption. They cover the required data, infrastructure, configuration, responsibilities and recovery procedures. |
| Recovery Point Objective (RPO) / Recovery Time Objective (RTO) | RPO expresses acceptable data loss in time. RTO expresses the target time for restoring service. Achieving these objectives depends on implemented and tested recovery arrangements. |
| Operational evidence | A dated configuration record, measurement or test result supporting a specific technical claim. Its meaning depends on the environment, time and functions covered. |
| Service Desk (ECCCH support service) | The support service through which users report problems and request assistance. Tickets record requests, progress and escalation to responsible teams. Zammad is the software implementation selected for the ECCCH Service Desk. |

## Related reference

[ECHOES Glossary](https://github.com/ECHOES-ECCCH-TECHNICAL/ECHOES-Glossary)
