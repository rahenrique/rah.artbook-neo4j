// Optional Cleanup:
MATCH (n) DETACH DELETE n;

// Techniques
CREATE (oleo:Technique {name:"Óleo sobre tela"})
CREATE (gravura:Technique {name:"Gravura"})
CREATE (aguaforte:Technique {name:"Água-forte"})
CREATE (aguatinta:Technique {name:"Água-tinta"})
CREATE (pontaseca:Technique {name:"Ponta seca"})

// Artists
CREATE (picasso:Artist {uuid:"e0a08a2b-f415-48dd-8d30-c792949c3f5e",name:"Pablo Picasso",birth:date("1881-10-25"),death:date("1973-04-08"),alternative_names:["Pablo Ruiz Picasso"]})
CREATE (portinari:Artist {uuid:"3b4fb595-746b-48dc-8953-4c9487c75e59",name:"Candido Portinari",birth:date("1903-12-29"),death:date("1962-02-06")})
CREATE (tarsila:Artist {uuid:"2bcf994f-50a7-49fa-92fa-61be3f8aa0bd",name:"Tarsila do Amaral",birth:date("1886-09-01"),death:date("1973-01-17"),alternative_names:["Tarsila de Aguiar do Amaral"]})
CREATE (monet:Artist {uuid:"777c72fc-6104-4b92-8319-170f4c8044f1",name:"Claude Monet",birth:date("1840-11-14"),death:date("1926-12-05"),alternative_names:["Oscar-Claude Monet"]})
CREATE (vangogh:Artist {uuid:"be7c535c-e630-4f77-96e4-5a5dd92dd94c",name:"Vincent Van Gogh",birth:date("1853-03-30"),death:date("1890-07-29"),alternative_names:["Vincent Willem van Gogh"]})
CREATE (goya:Artist {uuid:"e786078a-301b-4c36-ab19-0dac079e3f87",name:"Francisco Goya",birth:date("1746-03-30"),death:date("1828-04-16"),alternative_names:["Francisco José de Goya y Lucientes","Goya, o Turbulento","Francisco de los Toros"]})

// Artworks
CREATE (guernica:Artwork {uuid:"9e6e1552-72e1-4deb-b60e-a8b5ceb23ddd",title:"Guernica",creation:date("1937-01-01")})
CREATE (demoiselles:Artwork {uuid:"4bb7583d-1973-4f16-a573-70ed690ffbc5",title:"Les demoiselles d'Avignon",creation:date("1907-01-01")})
CREATE (sol:Artwork {uuid:"724b78cf-2704-4bd7-a4bf-e230b5156d69",title:"Impressão, nascer do sol",creation:date("1872-01-01")})
CREATE (noite:Artwork {uuid:"7884dd53-d67c-4d81-80a9-eca57dcf1cb4",title:"A Noite Estrelada",creation:date("1889-01-01")})
CREATE (retirantes:Artwork {uuid:"31d9a2ad-946b-4dba-8c5f-ff2dc00781bb",title:"Os Retirantes",creation:date("1944-01-01")})
CREATE (abaporu:Artwork {uuid:"137d1dbb-750d-49dc-9345-31e6651aba3d",title:"Abaporu",creation:date("1928-01-01")})
CREATE (tauromaquia1:Artwork {uuid:"cb868c36-a30f-4e9c-a4d6-41705d33033c",title:"No. 1: Modo con que los antiguos Espanoles cazaban los toros a caballo en el campo",creation:date("1816-01-01")})
CREATE (tauromaquia2:Artwork {uuid:"83fe624e-3ea6-4fdb-8ad7-cf75933e7deb",title:"No. 2: Otro modo de cazar a pie",creation:date("1816-01-01")})
CREATE (tauromaquia3:Artwork {uuid:"8186b710-b47c-408b-a14e-c23fa16de27e",title:"No. 18: Temeridad de Martincho en la plaza de Zaragoza",creation:date("1816-01-01")})
CREATE (tauromaquia4:Artwork {uuid:"cc03d74f-8f58-4b3c-a7e9-8fc69e616a85",title:"No. 21: Desgracias acaecidas en el tendido de la plaza de Madrid, y muerte del alcalde de Torrejón",creation:date("1816-01-01")})
CREATE (tauromaquia5:Artwork {uuid:"66018230-a5a9-4712-8907-b6e230542d01",title:"No. 31: Banderillas de fuego",creation:date("1816-01-01")})
CREATE (sonho:Artwork {uuid:"68061858-a0ec-45b7-9722-3ba726adb7ff",title:"Capricho No. 43: El sueño de la razón produce monstruos",creation:date("1799-01-01")})
CREATE (sastre:Artwork {uuid:"6000fdca-7ccc-42d6-86d0-fe8e0ebc0bf1",title:"Capricho No. 52: ¡Lo que puede un sastre!",creation:date("1799-01-01")})

// Authorships
CREATE (picasso)-[:AUTHOR_OF]->(guernica)
CREATE (picasso)-[:AUTHOR_OF]->(demoiselles)
CREATE (portinari)-[:AUTHOR_OF]->(retirantes)
CREATE (tarsila)-[:AUTHOR_OF]->(abaporu)
CREATE (monet)-[:AUTHOR_OF]->(sol)
CREATE (vangogh)-[:AUTHOR_OF]->(noite)
CREATE (goya)-[:AUTHOR_OF]->(tauromaquia1)
CREATE (goya)-[:AUTHOR_OF]->(tauromaquia2)
CREATE (goya)-[:AUTHOR_OF]->(tauromaquia3)
CREATE (goya)-[:AUTHOR_OF]->(tauromaquia4)
CREATE (goya)-[:AUTHOR_OF]->(tauromaquia5)
CREATE (goya)-[:AUTHOR_OF]->(sonho)
CREATE (goya)-[:AUTHOR_OF]->(sastre)

// Artwork Techniques
CREATE (guernica)-[:USES_TECHNIQUE]->(oleo)
CREATE (demoiselles)-[:USES_TECHNIQUE]->(oleo)
CREATE (sol)-[:USES_TECHNIQUE]->(oleo)
CREATE (noite)-[:USES_TECHNIQUE]->(oleo)
CREATE (retirantes)-[:USES_TECHNIQUE]->(oleo)
CREATE (abaporu)-[:USES_TECHNIQUE]->(oleo)
CREATE (tauromaquia1)-[:USES_TECHNIQUE]->(gravura)
CREATE (tauromaquia1)-[:USES_TECHNIQUE]->(aguaforte)
CREATE (tauromaquia1)-[:USES_TECHNIQUE]->(aguatinta)
CREATE (tauromaquia2)-[:USES_TECHNIQUE]->(gravura)
CREATE (tauromaquia2)-[:USES_TECHNIQUE]->(aguaforte)
CREATE (tauromaquia2)-[:USES_TECHNIQUE]->(aguatinta)
CREATE (tauromaquia3)-[:USES_TECHNIQUE]->(gravura)
CREATE (tauromaquia3)-[:USES_TECHNIQUE]->(aguaforte)
CREATE (tauromaquia4)-[:USES_TECHNIQUE]->(gravura)
CREATE (tauromaquia5)-[:USES_TECHNIQUE]->(gravura)
CREATE (tauromaquia5)-[:USES_TECHNIQUE]->(aguaforte)
CREATE (tauromaquia5)-[:USES_TECHNIQUE]->(aguatinta)
CREATE (sonho)-[:USES_TECHNIQUE]->(gravura)
CREATE (sonho)-[:USES_TECHNIQUE]->(aguatinta)
CREATE (sonho)-[:USES_TECHNIQUE]->(pontaseca)


// Artwork Series
CREATE (tauros:ArtworkSeries{uuid:"8bc1271d-7cc8-4ae1-898d-6883949d7174",name:"La Tauromaquia"})
CREATE (tauromaquia1)-[:BELONGS_TO]->(tauros)
CREATE (tauromaquia2)-[:BELONGS_TO]->(tauros)
CREATE (tauromaquia3)-[:BELONGS_TO]->(tauros)
CREATE (tauromaquia4)-[:BELONGS_TO]->(tauros)
CREATE (tauromaquia5)-[:BELONGS_TO]->(tauros)

CREATE (caprichos:ArtworkSeries{uuid:"f5a82931-3910-4f19-83e3-4feb31926236",name:"Los Caprichos"})
CREATE (sonho)-[:BELONGS_TO]->(caprichos)
CREATE (sastre)-[:BELONGS_TO]->(caprichos)


// Artist Collectives
CREATE (cinco:ArtistCollective {uuid:"be577880-6b7c-47c3-afcb-9661b399b187",name:"Grupo dos Cinco",foundation:date("1922-01-01"),end:date("1929-01-01"),alternative_names:["Group of Five"]})
CREATE (tarsila)-[:MEMBER_OF]->(cinco)

// Events
CREATE (evt1:Event {uuid:"2639dc5a-b5c5-4525-86b1-5486545bfee4",start:date("2018-01-01"),end:date("2018-06-01"),title:"Exposição 2018"})
CREATE (evt2:Event {uuid:"21697015-8f0a-47a1-a0da-763cd2e0e9c7",start:date("2020-01-05"),end:date("2020-07-15"),title:"Exposição 2020"})
CREATE (evt3:Event {uuid:"9a42a625-2c3b-48ee-a4a4-afc67f6de6fe",start:date("2019-02-15"),end:date("2019-05-15"),title:"Exposição 2019"});