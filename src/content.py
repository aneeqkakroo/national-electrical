"""All site content lives here. Edit this file, then run build.py."""

BUSINESS = {
    "name": "National Electrical Ltd",
    "domain": "nationalelectrical.uk",
    "url": "https://nationalelectrical.uk",
    "phone": "07344 988182",
    "phone_tel": "+447344988182",
    "whatsapp": "447344988182",  # WhatsApp number in international format, no + or spaces
    "email": "info@nationalelectrical.uk",
    "hours": "Mon–Fri 8am–6pm · Sat 9am–1pm",
    "hours_schema": ["Mo-Fr 08:00-18:00", "Sa 09:00-13:00"],
    "region_line": "Cambridgeshire, the East of England & Greater London",
    "company_no": "",  # Companies House number, e.g. "16123456". Legally required on the site.
    "registered_office": "",  # Registered office address. Legally required on the site.
    "scheme": "",  # e.g. "NICEIC Approved Contractor". Leave blank until registered.
}

# Draft banner shown on every page until these are filled in. Set to "" to remove.
DRAFT_NOTE = ""

# ---------------------------------------------------------------- services
# group -> (label, icon key)
GROUPS = [
    ("install", "Electrical installation", "install"),
    ("testing", "Testing & inspection", "testing"),
    ("design", "Electrical design", "design"),
    ("repairs", "Repairs & emergencies", "repairs"),
    ("renew", "EV & renewables", "renew"),
    ("safety", "Safety, security & data", "safety"),
]

SERVICES = [
  {
    "slug": "electrical-installation", "group": "install",
    "name": "Electrical installation",
    "short": "New circuits, sockets, lighting, kitchens, extensions and new builds.",
    "meta": "Electrical installation for homes and businesses in Cambridgeshire, the East of England and London. New circuits, lighting, sockets, extensions and new builds, fully certified.",
    "h1": "Electrical installation, <em>tested and certified</em>",
    "intro": "Whether it's a few extra sockets or the full wiring for a new build, we plan the work properly, install it neatly and test every circuit before we hand it over.",
    "includes": ["New circuits and sockets", "Indoor and outdoor lighting", "Kitchen and bathroom wiring", "Extensions and loft conversions", "New-build first and second fix", "Garden rooms, garages and outbuildings", "Electric showers and cooker circuits", "Electrical Installation Certificate (EIC)"],
    "sections": [
      ("Planned before we start", "We visit, look at your existing installation and agree exactly where everything goes. If your consumer unit or earthing needs upgrading to take new circuits safely, we'll tell you at quote stage, not halfway through the job."),
      ("Certified and notified", "New circuits and work in bathrooms are notifiable under Part P of the Building Regulations. We register the work with Building Control for you and give you an Electrical Installation Certificate, which you'll need when you sell the property."),
    ],
    "faqs": [
      ("Do I need a certificate for new electrical work?", "Yes. All new electrical work should come with a certificate. Smaller jobs get a Minor Electrical Installation Works Certificate; new circuits get a full Electrical Installation Certificate."),
      ("Can you work alongside my builder?", "Yes. We regularly do first fix while walls are open and come back for second fix after plastering. Tell us your build schedule and we'll fit around it."),
    ],
    "related": ["rewiring", "consumer-unit-upgrades", "electrical-design"],
  },
  {
    "slug": "rewiring", "group": "install",
    "name": "House rewiring",
    "short": "Full and partial rewires for older homes, flats and HMOs.",
    "meta": "Full and partial house rewires in Cambridgeshire, the East of England and London. Clear fixed quotes, tidy work, Part P certified.",
    "h1": "Full and partial <em>house rewires</em>",
    "intro": "Old wiring is one of the most common causes of electrical fires. If your home still has rubber or fabric-insulated cable, a wooden-backed fuse board or no earthing to the lighting, it's probably time for a rewire.",
    "includes": ["Full and partial rewires", "New consumer unit with RCBO protection", "Updated earthing and bonding", "Extra sockets where you need them", "Mains-wired smoke and heat alarms", "Lighting and switch replacement", "Making good and tidy finish", "EIC and Part P notification"],
    "sections": [
      ("Signs your home needs a rewire", "Black rubber or fabric cable, round-pin sockets, sockets on skirting boards, a fuse box with wire fuses, frequent tripping, or a recent EICR coded C2 for the wiring. Most homes need rewiring every 25 to 30 years."),
      ("How long it takes", "A typical three-bedroom house takes five to eight working days. We work room by room so you keep power and lighting overnight in most cases, and we lift and relay floorboards carefully."),
    ],
    "faqs": [
      ("Can I stay in the house during a rewire?", "Usually, yes. We plan the work so you have power and lighting at the end of each day. Empty homes are quicker, so if you're between tenants or moving in, that's the best time."),
      ("Will you need to damage the walls?", "Cables are chased into walls where needed and we make good with filler, ready for decorating. Plastering and decorating are not usually included, but we can recommend local trades."),
      ("Do I need a partial or full rewire?", "If part of your wiring was replaced recently and tests well, a partial rewire can save money. We'll test first and tell you honestly which you need."),
    ],
    "related": ["consumer-unit-upgrades", "eicr", "electrical-installation"],
  },
  {
    "slug": "consumer-unit-upgrades", "group": "install",
    "name": "Consumer unit upgrades",
    "short": "Replace old fuse boxes with modern RCD and RCBO protected boards.",
    "meta": "Consumer unit and fuse box upgrades in Cambridgeshire, the East of England and London. Metal RCBO boards with surge protection, fully tested and certified.",
    "h1": "Consumer unit and <em>fuse box upgrades</em>",
    "intro": "Your consumer unit (fuse board) protects every circuit in the building. Older boards often have no RCD protection against electric shock, and plastic boards fitted before 2016 don't meet the current requirement for non-combustible enclosures.",
    "includes": ["Metal (non-combustible) consumer unit", "RCBO protection on every circuit", "Surge protection device (SPD)", "Earthing and bonding checks", "Testing of every circuit", "Clear circuit labelling", "Part P notification", "Electrical Installation Certificate"],
    "sections": [
      ("Why RCBOs", "An RCBO combines shock protection and overload protection for one circuit. If a fault trips a circuit, only that circuit goes off, not half the house. It's the option we recommend for most homes."),
      ("Testing comes first", "A new board will show up faults that an old one hid. We test the existing circuits before quoting, so you know about any problems before the work starts."),
    ],
    "faqs": [
      ("How long does a consumer unit change take?", "Most domestic boards take one day. The power is off for most of that time, and we'll agree a start time with you."),
      ("My board keeps tripping. Do I need a new one?", "Not always. Tripping usually means a fault on a circuit or an appliance. We'll find the fault first. See fault finding and repairs."),
    ],
    "related": ["fault-finding-repairs", "rewiring", "eicr"],
  },
  {
    "slug": "commercial-electrical", "group": "install",
    "name": "Commercial electrical",
    "short": "Fit-outs, maintenance and compliance for offices, shops and hospitality.",
    "meta": "Commercial electricians for offices, shops, restaurants and schools across Cambridgeshire, the East of England and London. Fit-outs, maintenance and testing.",
    "h1": "Commercial electrical <em>contracting</em>",
    "intro": "We fit out and look after offices, shops, restaurants, clinics and schools. We can work evenings and weekends so your business keeps trading.",
    "includes": ["Office and retail fit-outs", "Restaurant and kitchen installations", "LED lighting upgrades", "Distribution boards and sub-mains", "Small power and data", "Emergency lighting and fire alarms", "Planned maintenance contracts", "EICR and PAT testing"],
    "sections": [
      ("One contractor for the whole building", "From the main switch to the last LED panel, we handle design, installation, testing and certification. You get one point of contact and one set of documents for your building file."),
      ("Lower running costs", "Replacing old fluorescent fittings with LED panels and adding presence detection often pays for itself in two to three years. We'll give you a lighting survey with estimated savings."),
    ],
    "faqs": [
      ("Do you provide RAMS?", "Yes. We provide risk assessments and method statements before work starts, and we're used to working on occupied sites."),
      ("Can you take over maintenance of our building?", "Yes. We offer planned maintenance contracts that cover periodic testing, emergency lighting tests and reactive call-outs."),
    ],
    "related": ["fire-alarms-emergency-lighting", "pat-testing", "electrical-design"],
  },
  {
    "slug": "industrial-electrical", "group": "install",
    "name": "Industrial & three-phase",
    "short": "Three-phase supplies, machine wiring, distribution and containment.",
    "meta": "Industrial electricians in Cambridgeshire, the East of England and London. Three-phase installations, machine wiring, distribution boards and containment.",
    "h1": "Industrial and <em>three-phase</em> installations",
    "intro": "Warehouses, workshops, farms and factories need robust installations designed for heavy loads. We install and maintain three-phase systems, from new supplies to machine connections.",
    "includes": ["Three-phase supplies and distribution", "Machine and equipment wiring", "Steel containment, tray and trunking", "SWA and sub-main cabling", "High-bay LED lighting", "Isolation and emergency stop circuits", "Power factor and load surveys", "Periodic inspection (EICR)"],
    "sections": [
      ("Designed for the load", "We calculate cable sizes, protective devices and discrimination for your actual loads, so equipment starts reliably and faults don't take out the whole site."),
      ("Subcontract work", "We work as the electrical subcontractor for main contractors, with full design calculations, test results and O&M documentation at handover."),
    ],
    "faqs": [
      ("How often should an industrial installation be tested?", "IET guidance recommends a periodic inspection at least every three years for industrial premises, and more often where conditions are harsh."),
    ],
    "related": ["electrical-design", "commercial-electrical", "eicr"],
  },
  {
    "slug": "eicr", "group": "testing",
    "name": "EICR & periodic inspection",
    "short": "Electrical Installation Condition Reports for homes and businesses.",
    "meta": "EICR electrical inspection and testing in Cambridgeshire, the East of England and London. Clear reports, fast turnaround and remedial work if needed.",
    "h1": "EICR and <em>periodic inspection</em>",
    "intro": "An Electrical Installation Condition Report (EICR) is a thorough check of your fixed wiring: circuits, sockets, switches, protective devices, earthing and bonding. It tells you whether the installation is safe to keep using.",
    "includes": ["Visual inspection of the whole installation", "Testing of every circuit", "RCD and protective device tests", "Earthing and bonding checks", "Clear coded report (C1, C2, C3, FI)", "Photos of any issues found", "Fixed quote for any remedial work", "Report emailed within 48 hours"],
    "sections": [
      ("When you need one", "When you buy or sell a property, before letting it, every five years for rented homes and commercial premises, every ten years for owner-occupied homes, or if you're worried about the condition of the wiring."),
      ("Satisfactory or unsatisfactory", "If any C1, C2 or FI codes are found the report is unsatisfactory. We'll explain each item in plain English, give you a fixed price to put it right, and issue the paperwork once it's done."),
    ],
    "codes": True,
    "faqs": [
      ("How long does an EICR take?", "A typical flat takes two to three hours and a three-bedroom house three to four hours. The power will be off at times during testing."),
      ("Is an EICR the same as a landlord safety certificate?", "Yes. 'Landlord electrical safety certificate' is the common name for an EICR on a rented property."),
    ],
    "related": ["landlord-certificates", "pat-testing", "consumer-unit-upgrades"],
  },
  {
    "slug": "landlord-certificates", "group": "testing",
    "name": "Landlord electrical certificates",
    "short": "EICRs and remedial work for landlords, HMOs and letting agents.",
    "meta": "Landlord electrical safety certificates (EICR) in Cambridgeshire, the East of England and London. Remedial work within 28 days. Letting agents welcome.",
    "h1": "Landlord <em>electrical safety</em> certificates",
    "intro": "Private landlords in England must have the electrical installation in rented homes inspected and tested at least every five years. We make it simple: book the EICR, we do the test, fix anything that needs fixing and send you the paperwork.",
    "includes": ["EICR for flats, houses and HMOs", "Access arranged directly with tenants", "Remedial work quoted on the day", "Confirmation of completed remedial work", "Mains-wired smoke and CO alarms", "Reminders before your next test is due", "Portfolio and agent scheduling", "Reports sent to you and your agent"],
    "sections": [
      ("What the law requires", "Under the Electrical Safety Standards in the Private Rented Sector (England) Regulations 2020, you must have the installation tested at least every five years, give a copy of the report to existing tenants within 28 days, give it to new tenants before they move in, and supply it to the local council within seven days if they ask."),
      ("If remedial work is needed", "Any C1, C2 or FI items must be put right within 28 days, or sooner if the report says so. You then need written confirmation that the work is complete. We provide that confirmation with a certificate for the work."),
    ],
    "codes": True,
    "faqs": [
      ("Can you deal with my tenants directly?", "Yes. Give us their contact details and we'll arrange access, so you don't have to."),
      ("Do HMOs need anything extra?", "HMOs often need fire alarm systems and emergency lighting too, depending on size and your council's licensing conditions. We can check and quote for everything in one visit."),
    ],
    "related": ["eicr", "fire-alarms-emergency-lighting", "fault-finding-repairs"],
  },
  {
    "slug": "pat-testing", "group": "testing",
    "name": "PAT testing",
    "short": "Portable appliance testing for offices, shops, schools and landlords.",
    "meta": "PAT testing for businesses and landlords in Cambridgeshire, the East of England and London. Labelled appliances and a full digital register.",
    "h1": "PAT testing for <em>businesses and landlords</em>",
    "intro": "Portable appliance testing checks that kettles, computers, extension leads and other plug-in equipment are safe to use. It helps you meet your duty under the Electricity at Work Regulations and keeps your insurer happy.",
    "includes": ["Visual inspection of every appliance", "Electrical testing where needed", "Pass/fail label on each item", "Full digital asset register", "Minor repairs on site (plugs, fuses)", "Out-of-hours testing available", "Reminders when retesting is due", "Certificate for your records"],
    "sections": [
      ("How often to test", "There's no fixed legal interval. The IET Code of Practice recommends a risk-based approach: heavy-use equipment on building sites needs checking far more often than a monitor in an office. We'll recommend a schedule for your premises."),
    ],
    "faqs": [
      ("Do landlords need PAT testing?", "It isn't a legal requirement for rented homes, but it's recommended for any appliances you supply, and many letting agents ask for it."),
      ("Will it disrupt our office?", "Each item is only unplugged for a minute or two. We can work early, late or at weekends if needed."),
    ],
    "related": ["eicr", "commercial-electrical", "landlord-certificates"],
  },
  {
    "slug": "electrical-design", "group": "design",
    "name": "Electrical design",
    "short": "Design, drawings and calculations for builders, architects and businesses.",
    "meta": "Electrical design services in Cambridgeshire, the East of England and London. Layouts, cable calculations, lighting design and distribution design to BS 7671.",
    "h1": "Electrical design to <em>BS 7671</em>",
    "intro": "Good installations start with good design. We produce layouts, calculations and specifications for extensions, new builds, commercial fit-outs and industrial projects.",
    "includes": ["Power and lighting layouts", "Cable sizing and voltage-drop calculations", "Fault level and discrimination studies", "Distribution and schematic drawings", "Lighting design and lux calculations", "Maximum demand and supply assessments", "DNO supply applications", "Specifications for tender"],
    "sections": [
      ("Who it's for", "Architects and builders who need an electrical package, businesses planning a fit-out, and homeowners with a large project such as a new build or major extension."),
      ("Design and install, or design only", "We can design and then install the work ourselves, or provide a design package for another contractor to price and build."),
    ],
    "faqs": [
      ("Do I need a supply upgrade?", "If you're adding EV chargers, heat pumps or a large extension, your incoming supply may not be big enough. We'll calculate your maximum demand and apply to the network operator if needed."),
    ],
    "related": ["commercial-electrical", "industrial-electrical", "electrical-installation"],
  },
  {
    "slug": "fault-finding-repairs", "group": "repairs",
    "name": "Fault finding & repairs",
    "short": "Tripping circuits, dead sockets, flickering lights and other faults.",
    "meta": "Electrical fault finding and repairs in Cambridgeshire, the East of England and London. Tripping RCDs, dead sockets, lighting faults. Fast, fixed-price repairs.",
    "h1": "Electrical <em>fault finding</em> and repairs",
    "intro": "A tripping RCD, a dead socket or lights that flicker are signs that something is wrong. We trace the fault with the right test equipment, explain what we've found and fix it.",
    "includes": ["Tripping RCDs and breakers", "Dead sockets and circuits", "Flickering or failed lighting", "Burning smells and scorched fittings", "Damaged cables and accessories", "Faulty appliances and connections", "Water and storm damage", "Insurance reports"],
    "sections": [
      ("How we find faults", "We isolate circuits one at a time and use insulation resistance testing to narrow down the fault, rather than guessing and replacing parts. That usually means a quicker, cheaper fix."),
    ],
    "faqs": [
      ("My RCD trips when it rains. Why?", "Water is getting into an outdoor circuit, such as a garden socket, outside light or garage supply. Avoid using it and call us to trace and fix it."),
      ("Is a burning smell an emergency?", "Yes. Switch off at the consumer unit if it's safe to do so and call us straight away on the emergency line."),
    ],
    "related": ["emergency-electrician", "consumer-unit-upgrades", "eicr"],
  },
  {
    "slug": "emergency-electrician", "group": "repairs",
    "name": "Emergency electrician",
    "short": "Power loss, exposed wiring and burning smells. Call us to make it safe.",
    "meta": "Emergency electrician in Cambridgeshire, the East of England and London. Power loss, burning smells, exposed wiring and storm damage. Call 07344 988182.",
    "h1": "Emergency <em>electrician</em>",
    "intro": "If you've lost power, can smell burning or have exposed or damaged wiring, call us. An electrician will come out to make the installation safe and get the power back on where possible.",
    "includes": ["Complete or partial power loss", "RCD or breaker that won't reset", "Burning smell or scorch marks", "Exposed or damaged wiring", "Water leaks near electrics", "Storm and flood damage", "Make-safe after an accident", "Reports for insurers"],
    "sections": [
      ("What to do while you wait", "If it's safe, switch off at the main switch on your consumer unit. Don't touch damaged cables or anything wet. If the problem is with the meter or the supply cable outside, call your network operator on 105."),
    ],
    "callout": ("Power cut in the street?", "If your neighbours have also lost power, it's probably a supply fault. Call 105, the free national power cut number, before calling an electrician."),
    "faqs": [
      ("How quickly can you get here?", "It depends on where you are and the time of day. We'll give you an honest arrival time when you call."),
    ],
    "related": ["fault-finding-repairs", "consumer-unit-upgrades", "eicr"],
  },
  {
    "slug": "ev-chargers", "group": "renew",
    "name": "EV charger installation",
    "short": "Smart home chargers and workplace charging points.",
    "meta": "EV charger installation in Cambridgeshire, the East of England and London. Smart 7 kW home chargers and workplace charging, installed and certified.",
    "h1": "EV charger <em>installation</em>",
    "intro": "Charging at home overnight is the cheapest and easiest way to run an electric car. We install smart chargers on a dedicated circuit, check that your supply can take the extra load and register the installation with your network operator.",
    "includes": ["7 kW smart home chargers", "Tethered or untethered units", "Dedicated circuit and protection", "Supply and load assessment", "Load management where needed", "Network operator notification", "Workplace and fleet chargers", "App setup and handover"],
    "sections": [
      ("Is my house suitable?", "Most homes with off-street parking can have a charger. We check your main fuse rating, earthing arrangement and consumer unit before quoting. Some older homes need a small upgrade first."),
      ("For businesses", "We install multiple charge points for staff and visitors, with load balancing so they share the available supply without overloading it."),
    ],
    "faqs": [
      ("Are there grants available?", "The government has offered chargepoint grants for some renters, flat owners and businesses. The schemes change, so we'll check what you're eligible for when you enquire."),
      ("How long does installation take?", "A standard home installation takes around half a day."),
    ],
    "related": ["solar-battery", "consumer-unit-upgrades", "electrical-design"],
  },
  {
    "slug": "solar-battery", "group": "renew",
    "name": "Solar PV & battery storage",
    "short": "Solar panels and home batteries to cut your energy bills.",
    "meta": "Solar PV and battery storage installation in Cambridgeshire, the East of England and London. Design, installation and network operator registration.",
    "h1": "Solar PV and <em>battery storage</em>",
    "intro": "Solar panels generate electricity during the day, and a battery stores it for the evening. Together they can cut your electricity bills substantially and pair well with an EV charger or heat pump.",
    "includes": ["Roof survey and system design", "Solar panel installation", "Hybrid inverters", "Battery storage systems", "Retrofit batteries for existing solar", "Network operator registration", "Monitoring app setup", "Electrical certification"],
    "sections": [
      ("Getting paid for exports", "Under the Smart Export Guarantee, energy suppliers pay you for electricity you send back to the grid. To qualify, the installation usually needs MCS certification. Ask us how we handle this for your system."),
    ],
    "faqs": [
      ("Can I add a battery to my existing panels?", "Yes, in most cases. We'll check your inverter and recommend either an AC-coupled battery or a hybrid inverter upgrade."),
    ],
    "related": ["ev-chargers", "electrical-design", "consumer-unit-upgrades"],
  },
  {
    "slug": "fire-alarms-emergency-lighting", "group": "safety",
    "name": "Fire alarms & emergency lighting",
    "short": "Design, installation and testing to BS 5839 and BS 5266.",
    "meta": "Fire alarm and emergency lighting installation and testing in Cambridgeshire, the East of England and London. BS 5839 and BS 5266 compliant.",
    "h1": "Fire alarms and <em>emergency lighting</em>",
    "intro": "We design, install, test and maintain fire detection and emergency lighting systems for homes, HMOs, offices, shops and industrial units.",
    "includes": ["Mains-wired smoke, heat and CO alarms", "Commercial fire alarm panels", "Domestic systems to BS 5839-6", "Commercial systems to BS 5839-1", "Emergency lighting to BS 5266-1", "Exit signs and escape route lighting", "Annual duration tests", "Logbooks and service certificates"],
    "sections": [
      ("Testing and servicing", "Emergency lights need a short functional test every month and a full-duration test every year. Fire alarm systems need regular servicing too. We can do this under a maintenance contract and keep your logbook up to date."),
    ],
    "faqs": [
      ("What does my HMO need?", "It depends on the number of storeys, occupants and your council's licensing conditions. We'll check your fire risk assessment and quote for a compliant system."),
    ],
    "related": ["landlord-certificates", "commercial-electrical", "security-data"],
  },
  {
    "slug": "security-data", "group": "safety",
    "name": "CCTV, security & data",
    "short": "CCTV, alarms, door entry, access control and network cabling.",
    "meta": "CCTV, intruder alarms, access control and data cabling in Cambridgeshire, the East of England and London.",
    "h1": "CCTV, security and <em>data cabling</em>",
    "intro": "We install the systems that protect your property and keep it connected: cameras, alarms, door entry, access control and structured data cabling.",
    "includes": ["HD and IP CCTV systems", "Intruder alarm systems", "Video door entry", "Access control", "Cat6 data and network cabling", "Wi-Fi access points", "Smart home and heating controls", "Surge protection"],
    "sections": [
      ("Planned with your power", "Because we're electricians first, we install the power, containment and data together, which saves you paying for two trades."),
    ],
    "faqs": [
      ("Can I view my cameras on my phone?", "Yes. All the CCTV systems we install can be viewed remotely, and we'll set up the app for you."),
    ],
    "related": ["fire-alarms-emergency-lighting", "commercial-electrical", "electrical-installation"],
  },
]

# ---------------------------------------------------------------- sectors
SECTORS = [
  {
    "slug": "homeowners", "tab": "Homeowners", "name": "Homeowners",
    "h1": "Electricians for <em>your home</em>",
    "meta": "Domestic electricians for homeowners in Cambridgeshire, the East of England and London. Rewires, consumer units, EV chargers, lighting and repairs.",
    "intro": "From a new socket to a full rewire, we work tidily, explain what we're doing and leave you with the right certificate. Notifiable work is registered with Building Control under Part P, so it won't cause problems when you sell.",
    "points": [("Tidy and respectful", "Dust sheets down, shoes off where asked, and we clear up every day."), ("Clear prices", "A fixed written quote before we start. No surprises on the invoice."), ("Certified work", "Every job is tested and certified, and Part P work is registered for you.")],
    "services": ["rewiring", "consumer-unit-upgrades", "ev-chargers", "electrical-installation", "fault-finding-repairs", "solar-battery"],
    "pills": [("rewiring", "Older homes"), ("consumer-unit-upgrades", "RCBO boards"), ("ev-chargers", "7 kW smart chargers"), ("electrical-installation", "Indoor & garden")],
    "cta": "Book a home visit",
  },
  {
    "slug": "landlords", "tab": "Landlords & agents", "name": "Landlords & letting agents",
    "h1": "Electrical compliance for <em>landlords and agents</em>",
    "meta": "Landlord EICRs, remedial work and HMO fire alarms in Cambridgeshire, the East of England and London. Letting agents and portfolios welcome.",
    "intro": "Private landlords in England must have the electrics in rented homes inspected at least every five years. We carry out the EICR, fix any C1, C2 or FI items, and send you the report and confirmation ready for your tenants and the council.",
    "points": [("We deal with tenants", "Send us their details and we'll arrange access directly."), ("28-day remedials", "Remedial work quoted on the day and completed within the legal deadline."), ("Never miss a renewal", "We keep track of your properties and remind you before tests are due.")],
    "services": ["landlord-certificates", "eicr", "fire-alarms-emergency-lighting", "pat-testing", "fault-finding-repairs", "rewiring"],
    "pills": [("landlord-certificates", "Every 5 years"), ("fault-finding-repairs", "Within 28 days"), ("fire-alarms-emergency-lighting", "Smoke, heat & CO"), ("pat-testing", "Supplied appliances")],
    "cta": "Book a landlord EICR",
  },
  {
    "slug": "businesses", "tab": "Businesses", "name": "Businesses",
    "h1": "Commercial electricians for <em>your business</em>",
    "meta": "Commercial electrical services for offices, shops, restaurants and schools in Cambridgeshire, the East of England and London.",
    "intro": "We fit out and maintain commercial premises with as little disruption as possible, working out of hours when needed. We also handle your compliance testing, so your insurer and fire risk assessment are covered.",
    "points": [("Out-of-hours working", "Evenings and weekends so you keep trading."), ("Compliance handled", "EICR, PAT, emergency lighting and fire alarm testing on one schedule."), ("One contact", "Design, install, test and maintain with one contractor.")],
    "services": ["commercial-electrical", "fire-alarms-emergency-lighting", "pat-testing", "eicr", "security-data", "ev-chargers"],
    "pills": [("commercial-electrical", "Offices, retail, hospitality"), ("fire-alarms-emergency-lighting", "BS 5266 & BS 5839"), ("pat-testing", "Asset register"), ("eicr", "Every 5 years")],
    "cta": "Request a site survey",
  },
  {
    "slug": "industrial", "tab": "Industrial & contractors", "name": "Industrial & contractors",
    "h1": "Industrial electrical and <em>subcontract work</em>",
    "meta": "Industrial electricians and electrical subcontractors in Cambridgeshire, the East of England and London. Three-phase, distribution and design.",
    "intro": "Three-phase supplies, distribution, containment and machine wiring, designed and installed by our team. We can work as your electrical subcontractor with full RAMS, design calculations and test documentation.",
    "points": [("Design included", "Cable, protection and discrimination calculations for your loads."), ("Site ready", "RAMS, method statements and qualified operatives."), ("Full handover", "Test results, drawings and O&M documentation.")],
    "services": ["industrial-electrical", "electrical-design", "eicr", "commercial-electrical", "fire-alarms-emergency-lighting", "ev-chargers"],
    "pills": [("industrial-electrical", "400 V three-phase"), ("electrical-design", "Design & calcs"), ("industrial-electrical", "Tray, basket, trunking"), ("eicr", "Every 3 years")],
    "cta": "Discuss a project",
  },
]

# ---------------------------------------------------------------- areas
AREAS = [
  {
    "slug": "cambridgeshire", "name": "Cambridgeshire", "home": True,
    "meta": "Electricians in Cambridge, Peterborough, Ely, Huntingdon, St Neots and across Cambridgeshire. Installation, design and testing.",
    "intro": "Cambridgeshire is our home county. We work in everything from Victorian terraces and student lets in Cambridge to new-build estates around Peterborough and farm buildings in the Fens.",
    "towns": {"Towns and cities": ["Cambridge", "Peterborough", "Ely", "Huntingdon", "St Neots", "St Ives", "Wisbech", "March", "Whittlesey", "Chatteris", "Soham", "Ramsey"],
              "Villages around Cambridge": ["Histon", "Cottenham", "Sawston", "Great Shelford", "Cambourne", "Northstowe", "Linton", "Bottisham"]},
    "postcodes": ["CB", "PE"],
    "local": "Cambridge has a large private rented sector, so landlord EICRs and HMO fire alarms make up a lot of our work there. Around Peterborough and Huntingdon we do more new-build, commercial unit and warehouse work.",
    "services": ["landlord-certificates", "rewiring", "ev-chargers", "commercial-electrical"],
  },
  {
    "slug": "suffolk", "name": "Suffolk",
    "meta": "Electricians in Bury St Edmunds, Newmarket, Ipswich, Haverhill and across Suffolk.",
    "intro": "From period cottages and listed buildings to yards and stables around Newmarket, Suffolk properties often need careful, sympathetic electrical work.",
    "towns": {"Towns": ["Bury St Edmunds", "Newmarket", "Ipswich", "Haverhill", "Sudbury", "Mildenhall", "Stowmarket", "Felixstowe", "Lowestoft", "Woodbridge"]},
    "postcodes": ["IP", "CB", "CO", "NR"],
    "local": "Older and rural properties often have outbuildings, private water supplies and long cable runs to garages and stables. We design these supplies properly, with the right cable and protection.",
    "services": ["rewiring", "eicr", "industrial-electrical", "solar-battery"],
  },
  {
    "slug": "norfolk", "name": "Norfolk",
    "meta": "Electricians in Norwich, King's Lynn, Thetford, Downham Market and across Norfolk.",
    "intro": "We cover Norwich, King's Lynn and the towns and villages of west and south Norfolk, including holiday lets, farms and rural homes.",
    "towns": {"Towns and cities": ["Norwich", "King's Lynn", "Thetford", "Downham Market", "Swaffham", "Dereham", "Wymondham", "Attleborough", "Diss", "Great Yarmouth"]},
    "postcodes": ["NR", "PE", "IP"],
    "local": "Holiday lets need regular electrical testing for insurance and safety, and many rural properties are good candidates for solar and battery systems.",
    "services": ["eicr", "solar-battery", "rewiring", "pat-testing"],
  },
  {
    "slug": "essex", "name": "Essex",
    "meta": "Electricians in Chelmsford, Colchester, Saffron Walden, Braintree and across Essex.",
    "intro": "From Saffron Walden and Uttlesford down to Chelmsford and Colchester, we work for homeowners, landlords and businesses across Essex.",
    "towns": {"Towns and cities": ["Chelmsford", "Colchester", "Saffron Walden", "Braintree", "Harlow", "Great Dunmow", "Witham", "Halstead", "Epping", "Brentwood"]},
    "postcodes": ["CM", "CO", "SS", "CB"],
    "local": "Commuter homes with home offices and EV chargers, and commercial units along the A12 and M11, make up most of our Essex work.",
    "services": ["ev-chargers", "consumer-unit-upgrades", "commercial-electrical", "landlord-certificates"],
  },
  {
    "slug": "hertfordshire", "name": "Hertfordshire",
    "meta": "Electricians in Royston, Stevenage, Hitchin, Bishop's Stortford and across Hertfordshire.",
    "intro": "We cover north and east Hertfordshire, from Royston and Hitchin to Stevenage, Hertford and Bishop's Stortford.",
    "towns": {"Towns": ["Royston", "Stevenage", "Hitchin", "Letchworth", "Baldock", "Bishop's Stortford", "Hertford", "Ware", "Welwyn Garden City", "St Albans"]},
    "postcodes": ["SG", "CM", "AL"],
    "local": "Offices, schools and family homes along the A1(M) corridor keep us busy with fit-outs, testing and EV charging work.",
    "services": ["commercial-electrical", "ev-chargers", "eicr", "fire-alarms-emergency-lighting"],
  },
  {
    "slug": "bedfordshire", "name": "Bedfordshire",
    "meta": "Electricians in Bedford, Biggleswade, Sandy, Luton and across Bedfordshire.",
    "intro": "We work across Bedfordshire, from Bedford and the market towns along the A1 to Luton and its industrial estates.",
    "towns": {"Towns": ["Bedford", "Biggleswade", "Sandy", "Luton", "Dunstable", "Leighton Buzzard", "Flitwick", "Ampthill", "Kempston"]},
    "postcodes": ["MK", "SG", "LU"],
    "local": "Warehouses and logistics units around the M1 and A1 need three-phase supplies, high-bay lighting and regular testing.",
    "services": ["industrial-electrical", "commercial-electrical", "eicr", "electrical-design"],
  },
  {
    "slug": "greater-london", "name": "Greater London",
    "meta": "Electricians across Greater London: North, East, Central, West and South London. Landlord EICRs, rewires, consumer units and commercial work.",
    "intro": "We work across Greater London for landlords, homeowners, managing agents and businesses. London's housing stock is full of Victorian and Edwardian conversions, flats and HMOs, so a lot of our work here is testing, rewiring and compliance.",
    "towns": {
      "North London": ["Barnet", "Enfield", "Haringey", "Islington", "Camden"],
      "East London": ["Hackney", "Tower Hamlets", "Newham", "Waltham Forest", "Redbridge", "Barking & Dagenham", "Havering"],
      "Central London": ["City of London", "Westminster", "Kensington & Chelsea"],
      "West London": ["Ealing", "Hammersmith & Fulham", "Hounslow", "Hillingdon", "Harrow", "Brent"],
      "South London": ["Lambeth", "Southwark", "Lewisham", "Greenwich", "Croydon", "Bromley", "Wandsworth", "Merton", "Sutton", "Kingston", "Richmond", "Bexley"],
    },
    "postcodes": ["E", "EC", "N", "NW", "SE", "SW", "W", "WC", "EN", "IG", "RM", "HA", "UB", "TW", "KT", "CR", "BR", "SM", "DA"],
    "local": "Many London boroughs run additional or selective licensing schemes for rented homes, which often ask for a current EICR and suitable fire detection. We can test, fix and certify everything a licence application needs in one visit.",
    "services": ["landlord-certificates", "rewiring", "consumer-unit-upgrades", "fire-alarms-emergency-lighting"],
  },
]

FAQS_GENERAL = [
  ("Are you qualified and registered?", "Yes. Our electricians are qualified to the current IET Wiring Regulations (BS 7671), and we make sure any notifiable work is signed off with Building Control under Part P, so you don't need to apply yourself."),
  ("Do you charge for quotes?", "No. Quotes are free and fixed. If we need to visit to give an accurate price, that visit is free too."),
  ("Which areas do you cover?", "We're based in Cambridgeshire and cover Suffolk, Norfolk, Essex, Hertfordshire, Bedfordshire and Greater London."),
  ("What certificate will I get?", "New circuits get an Electrical Installation Certificate (EIC). Smaller jobs get a Minor Electrical Installation Works Certificate. Inspections get an Electrical Installation Condition Report (EICR). Part P notifiable work also gets a Building Regulations compliance certificate."),
  ("Do you offer a guarantee?", "Yes. All our workmanship is guaranteed. Ask us for the details when you get your quote."),
  ("How do I pay?", "By bank transfer or card. For larger jobs we may ask for a deposit to order materials, and we'll agree any stage payments in writing first."),
  ("Do you work evenings and weekends?", "For commercial customers, yes, so your business can keep trading. For homes, we usually work weekdays but can be flexible."),
  ("How much notice do you need for an EICR?", "Usually a few days. If you have a tenancy deadline, tell us and we'll do our best to fit you in."),
]
