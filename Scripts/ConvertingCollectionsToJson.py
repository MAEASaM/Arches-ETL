import xml.etree.ElementTree as ET
import json

# Input XML data (replace with your XML content)
xml_data = """
<rdf:RDF>
<skos:Collection rdf:about="http://localhost:8000/c9f31ff6-0914-446d-95da-fb5bd3310e4b">
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/934b7316-c176-4232-95b5-80244cd459ff">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b3fce042-8eb6-43c4-849d-b4f22f954041"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/9adc4f4d-334e-4e7c-9ac8-75aaeb80c1d4"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/e06259eb-182d-4e08-a370-af58f8e7c35e"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "a96e7e4a-c519-4a42-b541-b7fbb562e673", "value": "Identifier Type"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/05e2754f-6960-45a3-b5ce-a8cadacb673d"/>
</skos:member>
<skos:scopeNote xml:lang="en">
{"id": "7fb9c4e1-84dd-4b30-9148-9add9dda3f13", "value": "This describes what type of identifier (describing an information resource) is specified in the adjacent identifier value attribute - for example, an ISBN number, a map sheet reference from a specific map series, or a DOI."}
</skos:scopeNote>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/9dc4d051-0e90-4ce5-b5a0-7971d97d3704"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/44f1b0e1-6438-425e-b2ef-152905c8228f"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/00000000-0000-0000-0000-000000000005">
<skos:prefLabel xml:lang="en">
{"id": "d8c622f6-e786-11e6-905a-475a5eee86f5", "value": "Resource To Resource Relationship Types"}
</skos:prefLabel>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/2cd5d1a1-5e13-4944-8060-56b5ec8b1f06">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/66389799-3138-4dfd-8728-9b710bc6d79b"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "3b51ea02-46e3-4a34-a1f6-144ee862071a", "value": "Evidence shape"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ab3a059a-4d7a-408e-905c-3d4298823496"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/225990ac-7eeb-48bc-be69-517cbdd2015b"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5a83a22c-3ce7-4486-af08-ec37344bee02"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1123b8a8-8648-418e-b70a-8f93917c782f"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/8beff696-68a7-41d1-a76e-5d4c907470e9"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1ecac167-95d6-44e4-b6a8-5a3cde618c02"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f60e52c5-5466-4636-9a32-93619b149387"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/dbe40b98-c347-48f2-85a5-f835b98d6455"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/3d22230c-ea19-4759-9a58-49b2d188f8d1">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b6b53c52-b5ac-445a-ac30-97bcf89e5343"/>
</skos:member>
<skos:prefLabel xml:lang="fr">
{"id": "2206edbd-cc98-4261-a6e4-e8eb7f5dce28", "value": "Imagerie"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/2678fdcb-40e2-4304-885f-1a3f1cacd452"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/503d4f0a-98d8-42d6-be5b-b07388672fac">
<skos:member rdf:resource="http://localhost:8000/69490585-9d61-4039-9057-d147263fa14f"/>
<skos:member rdf:resource="http://localhost:8000/ae7a4977-9d1e-43f9-945a-591adef5cbdc"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/11b672df-bcf4-48ad-8ad8-2e81a1146932">
<skos:member rdf:resource="http://localhost:8000/61671c1d-b6b3-4af9-a329-cd5609eed336"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/cab620da-1eb2-46b5-98e9-084bfd3815e7"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/03c8a48e-6100-4367-ad7d-7ff80158df87"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/fe9a7ea8-e62c-4ea5-811d-242d5ff35a71"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f4bef361-e671-4841-8bed-89f4cc51980f"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/cadfd850-d8e9-4124-a769-8d500f646464">
<skos:member rdf:resource="http://localhost:8000/d7f8892b-a97f-49f4-9d25-9f7400333e68"/>
<skos:member rdf:resource="http://localhost:8000/068a05c1-bd3e-4619-bb25-24b225321657"/>
<skos:member rdf:resource="http://localhost:8000/402c5ea6-5fb6-4595-8635-d92062a38a3f"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/365c21e2-50fc-4ab7-9f64-1eb5dbf51cd3">
<skos:member rdf:resource="http://localhost:8000/6a3c8e77-0bbb-4010-aacc-3a3cafc22fd8"/>
<skos:member rdf:resource="http://localhost:8000/70554156-baa3-4de8-9fff-85c2f54075cc"/>
<skos:member rdf:resource="http://localhost:8000/85689c7a-9dc8-46ae-a7c4-feb3fd2edc38"/>
<skos:member rdf:resource="http://localhost:8000/2f2c9d01-ff0d-45c3-9137-d9488f8cc078"/>
<skos:member rdf:resource="http://localhost:8000/1b0b8e08-c4ac-496e-8db0-1adf02bbd5cc"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/bd4c777e-44a5-413f-8cb6-da2924d7f7e8">
<skos:member rdf:resource="http://localhost:8000/6ff4dfd8-2e5b-4f26-9472-5a2422f7f04b"/>
<skos:member rdf:resource="http://localhost:8000/89f9e471-c574-40d2-882c-fab9d6f37b8b"/>
<skos:member rdf:resource="http://localhost:8000/e46ea77b-b791-4ca9-a891-f15cc7813ae3"/>
<skos:member rdf:resource="http://localhost:8000/22ee00ba-cd80-4b3d-9367-141be24a2f16"/>
</skos:Concept>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "f94d8802-2e7f-443a-afd4-1bbacebc5435", "value": "Imagery"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/cd0d202d-55ee-4e09-9fcb-5a98da4a425b">
<skos:member rdf:resource="http://localhost:8000/e34f9e36-0afa-40a0-b525-d7c30ed9da0c"/>
<skos:member rdf:resource="http://localhost:8000/cf2ab0f7-3bb6-4f91-8c61-a068ddd4a69b"/>
<skos:member rdf:resource="http://localhost:8000/6218920a-0e7e-48a5-9698-e7b88e664f47"/>
<skos:member rdf:resource="http://localhost:8000/e52e02e3-e182-4ddd-a5e9-8360971986ba"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/829ae8dd-b5b3-4ac4-92db-3d8cfc02e1e3">
<skos:member rdf:resource="http://localhost:8000/74ea067c-5813-4f10-8aa9-c6f6bb1ec128"/>
<skos:member rdf:resource="http://localhost:8000/fd370a17-49ed-4c5c-b609-cc1253ff1ecb"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/2cc25360-c5f3-42b6-9145-c52b6e90bf91"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/417656cd-8944-4899-95de-904cb4ee7fa9">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/217d506b-2ffd-4618-9b96-5025bb3de465">
<skos:member rdf:resource="http://localhost:8000/46ceafac-c7f1-4dbb-b653-62569ceb3bbd"/>
<skos:member rdf:resource="http://localhost:8000/194c0230-49de-4c8b-96a8-882f13d3ce2f"/>
<skos:member rdf:resource="http://localhost:8000/24d9fec0-31f4-4740-bbce-7a4397719960"/>
<skos:member rdf:resource="http://localhost:8000/ad2fbfbd-bde0-4587-a55a-d8937c86a715"/>
<skos:member rdf:resource="http://localhost:8000/d8dc6dad-0e63-444b-a0e3-0b82444b6349"/>
<skos:member rdf:resource="http://localhost:8000/b26b8bf9-c8be-45fb-afe6-35bb649eecdf"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/e8d08266-64b4-41a6-b569-a16fc1ed2f28">
<skos:member rdf:resource="http://localhost:8000/66559377-2317-40f4-958a-50e886cdf934"/>
<skos:member rdf:resource="http://localhost:8000/bf2cc9fa-8224-4035-a567-b9d9d6d96722"/>
</skos:Concept>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "88117bf1-5fd8-4d07-a6ab-aff5c3753a8a", "value": "Threat type"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/91d9eee8-ca60-4cfb-b445-32cabf4bfcfd"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f9e37619-9856-4089-bd6f-7f60d8837786"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/da8ddea8-61d9-439e-9d61-48bb59342552"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/7f1773bc-2696-4a8b-8cce-7ea8ac35b725">
<skos:member rdf:resource="http://localhost:8000/aa8f54f9-ba08-4243-b276-62a81805dda5"/>
<skos:member rdf:resource="http://localhost:8000/6af9ecff-8c4b-4fbc-9135-07eb5c24eb9a"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/206ee9d0-370b-487c-a1b7-8374fed93de1">
<skos:member rdf:resource="http://localhost:8000/7f0d45e4-598e-4f52-b0ca-ac3dc9403008"/>
<skos:member rdf:resource="http://localhost:8000/e9cd8e41-4616-436a-a190-5c2a4cfd6eab"/>
<skos:member rdf:resource="http://localhost:8000/011734b7-a0f6-44e9-acd5-57ff9e453be8"/>
<skos:member rdf:resource="http://localhost:8000/c0769f6e-209b-45b0-bd75-21a73b032a95"/>
<skos:member rdf:resource="http://localhost:8000/2bd93e3a-1bcb-4e2b-b59c-6eacdd27ba6c"/>
<skos:member rdf:resource="http://localhost:8000/a9639b7a-dd25-41e9-8ed0-ed5820dec17a"/>
<skos:member rdf:resource="http://localhost:8000/c37f78f0-ac78-49e9-8873-d4a50a591425"/>
<skos:member rdf:resource="http://localhost:8000/9035c4e3-693a-461e-b745-d9821aaa784c"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f215ea4e-5992-4b3b-8f8d-de254568f362">
<skos:member rdf:resource="http://localhost:8000/0c4000a8-5034-420b-a97b-d8915d773611"/>
<skos:member rdf:resource="http://localhost:8000/b7561b13-cc1d-4eb3-9d5a-b2f92e27c0cb"/>
<skos:member rdf:resource="http://localhost:8000/393a6aab-b744-4452-9530-653568c8d937"/>
<skos:member rdf:resource="http://localhost:8000/48aa8413-1ea2-416f-966c-de5c2bd3f249"/>
<skos:member rdf:resource="http://localhost:8000/6c1a0784-d6de-44c2-b4dc-b5ee984a4a7c"/>
<skos:member rdf:resource="http://localhost:8000/f1812ea4-a815-4a88-adfa-d72d08606354"/>
<skos:member rdf:resource="http://localhost:8000/403103e2-126b-4a0e-bba7-d109e2e1a15c"/>
<skos:member rdf:resource="http://localhost:8000/792850a2-c896-491d-b004-bfa4c5ac5e62"/>
<skos:member rdf:resource="http://localhost:8000/dc2337a4-b64b-423f-b845-965dae030ee5"/>
<skos:member rdf:resource="http://localhost:8000/2bc36055-ee70-4536-a076-ad77a09d9968"/>
<skos:member rdf:resource="http://localhost:8000/b7fe59a0-57c4-4796-ae14-8d7f7cbf4163"/>
<skos:member rdf:resource="http://localhost:8000/4f289bc6-9867-433d-837e-7ffe4c024ad5"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/e376d927-c2ab-4d12-9f76-1f916cfd205f">
<skos:member rdf:resource="http://localhost:8000/88ab9756-45b7-4dfb-8d60-523c21a3628f"/>
<skos:member rdf:resource="http://localhost:8000/374168a7-fabc-44bd-89f2-95bed49a0372"/>
<skos:member rdf:resource="http://localhost:8000/7ac05ac7-657c-45ea-8079-f99171111b1d"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/081e0dc2-339d-4b90-bb27-2a072a48d8aa">
<skos:member rdf:resource="http://localhost:8000/94d39278-730d-49c2-a6ef-c395b99f4fc6"/>
<skos:member rdf:resource="http://localhost:8000/dc9539f3-71bb-4aee-b0d0-d2f22eea9d23"/>
<skos:member rdf:resource="http://localhost:8000/166dada7-5318-4c5a-a9c8-7e545325be44"/>
<skos:member rdf:resource="http://localhost:8000/47cf2463-df9d-48ea-8021-3a6f2e586306"/>
</skos:Concept>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/cdc5495b-5d67-48b1-9695-aa28aa6456b9">
<skos:prefLabel xml:lang="fr">
{"id": "7df73e23-1461-4614-a22f-7b6883182115", "value": "Type d'informations"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f8be486e-2ce2-4868-8138-be19c0d74176"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/aba0070e-0e1d-410f-b157-7b0a18e9a310"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/d954ea04-2258-4612-808b-d21888c57a78"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/96734974-c88d-4067-89d4-338ff6bd2213"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/3920f3f1-0a0a-4621-b597-94d9be439393"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/3aef4271-73de-4d20-8b1e-4e154377b58b"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/af23f894-5829-42c4-b865-e2dce2b9546e"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/c20c253f-0a7f-4c30-86d2-35b13b0c03b2"/>
</skos:member>
<skos:scopeNote xml:lang="fr">
{"id": "7c78deab-b012-4305-82a5-aa1ee81578b3", "value": "Ceci d\u00e9crit le type de ressource d'information dans laquelle cette entr\u00e9e peut \u00eatre class\u00e9e - par exemple, une feuille de carte, un livre, un article de journal ou des notes de terrain."}
</skos:scopeNote>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/40468135-aed2-43a4-a00d-f02b3b933467"/>
</skos:member>
<skos:scopeNote xml:lang="en">
{"id": "2269a105-54f0-4be3-9da5-1c87048327a2", "value": "This describes the type of information resource which this entry can be classified as - for example a book, a journal article, or field notes."}
</skos:scopeNote>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/70690090-14ab-4342-b61d-8397154dcae6"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "731ec825-0517-4c1a-8035-107df6e83dff", "value": "Information Type"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/97483eca-8b30-4a9e-a88e-d3797a203ce2"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/99e57067-8108-4606-8a2c-b5f9979fb9a2"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/9c9ca24d-2708-4f97-aa8d-57525ad4cbf7">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/815f986c-e8a4-469e-91a8-8a9045f9f2e1"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/2046d69a-a991-4c98-9d94-80d51b42ec68"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/9e5a9de0-ff28-4688-a77b-5d7e4e22e919"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ae3e8f1f-a305-4042-b2e8-1fd51702fbc1"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/aad07056-387c-42cd-8629-6d1f5ef6fb10"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/20496f96-16ce-4e3e-94f3-00afb3e48188"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/9f29d2d3-55f8-42f7-94da-442c4a0ee1ee"/>
</skos:member>
<skos:prefLabel xml:lang="fr">
{"id": "b54e3e4b-c25e-4308-acf7-2b91ccdd9154", "value": "Origine des donn\u00e9es du site"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/a355fd92-9e22-49b5-9208-0cdfe3073e59"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "332948e8-1f13-49bd-9d45-391899e182d7", "value": "Origin of site data"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/bf95a1df-d94e-4fe1-bff7-7fe7280242ee"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ce1b7a9e-f6b0-4f04-b4cd-0fb616de35ef"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ea78f839-05c4-4b24-a4f5-60cb33871c57"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/29881c27-3344-4aa8-bfee-a6cf2c628cf1"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b53868e8-b872-4380-a035-703e1359b5db"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/0eccb779-5e4e-426e-bbbb-c759ec968444">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/816c3465-50dc-4b53-a4ca-5bb9dfbc9ae0"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/3656539b-ee3a-46e4-aa03-e0fdb31254e7"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5a48c15a-829a-4cd0-ad60-a91cdf1cec64"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "764debea-04be-43a9-8abe-e35afa58c852", "value": "Administration Official Division"}
</skos:prefLabel>
<skos:prefLabel xml:lang="sw">
{"id": "7c10b439-213a-4362-bb38-e45e91844dc3", "value": "Ngazi za utawala"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/588348ee-6288-4a56-8e4d-a0fa9e27b43f"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1ed46111-51d4-4045-aa84-f60329821efe"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b2ff8ea2-616c-46da-b397-374372deaec8"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/d2f77239-b83b-468b-92e8-ab67a3fc515e"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f6c14063-0495-4fd6-9bbc-f3b643a97698">
<skos:member rdf:resource="http://localhost:8000/290fe7c1-60a4-4cfd-b374-bf378a75a767"/>
<skos:member rdf:resource="http://localhost:8000/fbc90588-2a79-4cd3-8fa5-26ab452dd5a3"/>
</skos:Concept>
</skos:member>
<skos:prefLabel xml:lang="fr">
{"id": "e10b5d49-9068-4f5c-b391-316f25d6f7d5", "value": "Niveau de d\u00e9coupage administratif"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/76581382-c688-45a6-a815-57751a3ef353"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/20c336ae-172d-47dd-bdb4-db983ebe5c4b"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ff43446b-aaa5-4d55-b297-a2b816f66718"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b48e1e5d-b8e6-4503-b7dc-ab2b82758dc5"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/6ba9af9b-d342-4c97-b5ff-db479eada722"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/6b969ed7-0a70-4679-8fcc-69c02fece082">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/39fc78e3-107d-44da-a5a7-23c843b27099"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/af9bd55b-818d-41c1-8cd1-31845ccf184e"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/92b43423-7f97-40c1-b83e-5609536410bf"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "a5904642-1ebb-4304-b25c-08554dae6f1c", "value": "Density of material"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/46862b9a-37ec-43eb-8ad8-2d5dcbbfaef8"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/de7e4f50-627d-4106-95ec-1f13a10285d8"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/c747dc2f-abb9-4a07-807d-0854647c6096">
<skos:prefLabel xml:lang="en">
{"id": "8ab18fbf-e803-42c8-b320-d245cf7d2440", "value": "Administration Level"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/41c504f2-2f9e-48d7-bdbc-a2aac5d441cb"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/4e3fe4b3-8418-4430-a015-15e12944193f"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/e30dce91-8eb5-4a30-bc26-fd26eb096dd8"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/4d83ea96-795a-4439-8153-2876b139afa9"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/cd4e1b6e-a885-440c-bacc-ed672d37cc2d">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b08dc4f6-58ba-41c2-a2f5-16f51341c0a8"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1940de59-08b9-4a0a-9846-1721327cf6c0"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/6490b70a-ae69-4ed1-a495-9c101800bd37"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1658c4cb-1446-49f9-834c-f26aac2c3f14"/>
</skos:member>
<skos:prefLabel xml:lang="fr">
{"id": "489c8ef7-d0ed-45f9-b432-52fa9f19fef3", "value": "Type de mat\u00e9riel de surface (mat\u00e9riel artefactuel vu ou collect\u00e9)"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/fe19e88e-beb4-47e2-ac7d-27a7812fe234"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1bb6b183-f6d0-44f6-8322-47f3da47ab2c"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/cb55ff98-0343-4a53-af31-e7b16e17cbfa"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/c333ca56-5300-4f75-aae8-c5b9c00e7da4"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/c35e2f8b-150d-442c-a4f1-fd5d12887794"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/050638c5-3df5-4e66-aa8b-93db2260a9d8"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "a64494ae-8e0c-41a6-811c-53bc6ac0bd30", "value": "Surface material type (artefactual material seen or collected)"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/e0ea25d7-acee-4389-8bc7-82751e30e576"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/09e9ee84-0089-4342-a691-81947be64091"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5e590a11-c4b3-4009-b200-396becd1e482"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/324f5121-c115-4680-adc9-12b1493be0ac"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5f564dc2-89da-4415-9603-5985fc37e134"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/d7eb6941-b92a-41e6-a527-aadec94c4860"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/bbd65fea-7c4c-420f-9c99-bfad8e76f21e"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f882c879-cc18-463a-8309-003f8ad9bc80"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/8f208365-bb23-4b2a-9c0d-061f7b1bdb5f"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/2b2c7cb7-47a7-4b47-8c2d-232183e709d4"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/67f98279-aa62-4733-9719-883eda894efb"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/82d68b01-8ac0-47a4-8a93-c656cb90f563"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/375bd45b-4eda-4b8d-a48f-e9b1beffd4e9"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/31ad4847-12e0-45b6-81c3-27cdac5a6a67"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/36f59193-19cd-4293-8211-9729af69ed28"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/edc0c550-9260-4401-a7d4-4e00c891fd52"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/884891eb-13a7-4175-a8e4-8d4b2de4c9f2"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/cda2919e-8c4e-4d68-88cc-cd1774a1c2a8"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/c4c13391-2500-48fb-9edc-a17e4ba491a4"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/c56bb741-73f9-41ec-9b08-71701a1ef0fa">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5d1e217f-e357-437a-a7cb-1886dd02a2fe"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/d0e84c45-3fc0-4c00-bb51-afeaeb3dce73"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/3ed02fb4-d2df-4903-920b-44877b2a123c"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/af500701-28de-46e6-b4bb-ebb0cc5a6e9a"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "b60d6632-d9e0-47de-ba5a-a9d31637094a", "value": "Imagery source"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/dcb6db59-3829-45ed-ba24-b1afd97dc9de"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/741878f1-f064-4443-8e75-d381e956054b"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/8fd06ac8-2690-4527-8a9c-17ca4aa7c55f"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/57ca1e38-a472-4ef2-bca3-feb011652f07"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/dfb5159d-3413-4380-8d89-206ef70869c2"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/7273951c-7c23-4de8-a456-268a38a6315d"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5e038746-1af1-4f0f-a387-bfbb7fa78a39"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/d4c627f6-411a-4048-af2d-6930d9e5aa5c"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/16c57a67-0ce2-4b5c-80c0-4262a96f371d"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/70686564-a84e-4453-8e37-1fb173e4318b"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/70edf67b-b6cb-49d9-8b91-5c66892e7e18"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/88a2dbed-a846-40b0-97ec-000e8d544449"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5ad58699-c722-4074-9cf4-b253ee39e4be"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f821dc28-985d-4db0-8560-1159012ca79a"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/4ae13c41-4774-4b5d-89e2-91d0a63fb521">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/87b2cafe-1aa3-40af-bf98-55e583befd39"/>
</skos:member>
<skos:prefLabel xml:lang="fr">
{"id": "38b6ebca-ab7a-4be5-ac84-fb28f634cff6", "value": "R\u00e9sum\u00e9 du type de site"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/48fae927-6dd1-4cd3-acac-df134a007b72"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ce33ecc8-2983-4297-8872-91055aa1e4e0"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ad5e4ee5-7440-4651-9eba-23a6ad1caf81"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b335b032-fa90-4624-aa91-c2ddc7b077f5"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "79d0d94f-2c06-44b6-9ad5-a4eeb2e769e8", "value": "Site type summary"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/748d075d-57b5-44ef-acab-0edfe2a36dd3"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/24aa6ae8-512e-4216-b60a-d7963e4397e1">
<skos:prefLabel xml:lang="en">
{"id": "e01fa846-6e1c-40ff-99eb-6ea9823327c2", "value": "Image type"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/903ab8c3-4c07-4afb-b83c-be31e4997d9c">
<skos:member rdf:resource="http://localhost:8000/d2bf0a0d-921d-4e8d-b049-7f0d048f993f"/>
<skos:member rdf:resource="http://localhost:8000/5f107b39-285b-4ddd-a32d-53fc8891c17d"/>
<skos:member rdf:resource="http://localhost:8000/d53ff5d8-8166-4e8a-a92f-fbcfaf5983d6"/>
<skos:member rdf:resource="http://localhost:8000/3b103375-739a-4307-885f-0aeb47484a69"/>
<skos:member rdf:resource="http://localhost:8000/593a22c2-963c-4b27-9ce0-93af2d9aa3ea"/>
<skos:member rdf:resource="http://localhost:8000/fd9e102e-453f-43f2-965b-4e8e237cfd25"/>
<skos:member rdf:resource="http://localhost:8000/3c9bea82-eea0-49f8-a521-90fdb6d2e3a3"/>
<skos:member rdf:resource="http://localhost:8000/7a73602d-384f-4434-8794-50942ed40a6c"/>
<skos:member rdf:resource="http://localhost:8000/872dcd85-bf07-44ca-a2c5-d458ce3ef97c"/>
<skos:member rdf:resource="http://localhost:8000/532c5fec-bb23-4d94-86cd-aeef88f0f1c3"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/a94ec4a9-1adb-4e8f-bf05-2daa44710fbe"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1c7dbdb8-fa69-4bde-88e9-0e1d9c27fb8e"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/25a5ebde-0aad-4872-96f3-6409a74e798d"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/cb310ca9-e857-4945-a52f-dbcc4e80be65">
<skos:member rdf:resource="http://localhost:8000/f8e2e340-98d3-4bd8-9864-9070f4307553"/>
<skos:member rdf:resource="http://localhost:8000/c3ad28ce-a2d8-479a-b8f4-628e181f95ff"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/4b574305-6d4d-4f85-877f-18346ffd0611">
<skos:member rdf:resource="http://localhost:8000/758e60a5-01c3-4232-9f9b-2e9870f75429"/>
<skos:member rdf:resource="http://localhost:8000/a6a150db-67b2-4dd2-bc51-651a7c512009"/>
<skos:member rdf:resource="http://localhost:8000/a47027fb-0f2e-4ac4-a9ee-bfd88756b670"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/58b43eb8-9b0c-4e81-83db-4af221f575d7"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5fcad5fb-020b-44f9-ab27-4d55df58394d"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/fb315c87-3cfe-43fd-a7f7-2fb8cb87e055">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/8007dd9a-65b7-4f99-a95d-047a0993e972">
<skos:member rdf:resource="http://localhost:8000/d0e6f0c1-2233-4ebc-a089-7cd2a1fc3a42"/>
<skos:member rdf:resource="http://localhost:8000/b6ca0113-61e5-40fa-aedd-840836d1ff79"/>
<skos:member rdf:resource="http://localhost:8000/2b1d5702-5f07-455a-bd6e-5833baea3ea3"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/31f99a96-02dd-4914-9023-35ca1f37491e">
<skos:member rdf:resource="http://localhost:8000/3d8263e9-3a7d-404e-a92b-25536cf60133"/>
<skos:member rdf:resource="http://localhost:8000/d0b0aa26-afca-4602-abda-bc26e3d47ba8"/>
<skos:member rdf:resource="http://localhost:8000/3dcae09a-14d5-419e-a050-144e78fbe306"/>
</skos:Concept>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "386f99f3-ce55-4576-a547-4973b7a214b9", "value": "Climate zone"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/add67430-129d-4663-895d-631e7f3d6830">
<skos:member rdf:resource="http://localhost:8000/20e2bcb8-f00c-4aec-a086-26af53e37b7d"/>
<skos:member rdf:resource="http://localhost:8000/12050340-ef4b-499a-aa36-5b5783e255d8"/>
<skos:member rdf:resource="http://localhost:8000/2a8db864-9484-4c30-af80-7de4118e396a"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ac7effad-a2bf-4762-8162-49bcd649d0b9">
<skos:member rdf:resource="http://localhost:8000/d18fe978-60f2-462f-a6dc-b3fc6e310352"/>
<skos:member rdf:resource="http://localhost:8000/6ffc7e2e-088f-49cc-a71e-35452b341ee9"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/96174d1e-e5a2-4026-92b6-5e7b366402fd">
<skos:member rdf:resource="http://localhost:8000/46e56c73-cc44-409f-81f2-dd449ebf4def"/>
<skos:member rdf:resource="http://localhost:8000/da1e990b-6e0e-4d2f-9e9c-6c26ab77b0bb"/>
</skos:Concept>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/65d67714-55e5-4deb-8c52-c1bc6fcdc27e">
<skos:prefLabel xml:lang="en">
{"id": "1b387c7f-0a31-4207-a10f-b9dd6bf0ccdc", "value": "Land use land cover change"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/c6aac02a-7ed9-4e3d-b0f4-22a66f03fb74">
<skos:member rdf:resource="http://localhost:8000/bb9755fa-2da4-4beb-9447-acb45c2f7d5f"/>
<skos:member rdf:resource="http://localhost:8000/7c2728d4-4665-47dd-aa26-b7f7fdeedfa5"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/3837448b-ecf2-4cba-8204-b9eaa4a433c3">
<skos:member rdf:resource="http://localhost:8000/25de39cd-1250-48c0-8aa7-f7d5f1e5bbe2"/>
<skos:member rdf:resource="http://localhost:8000/6b4a2372-24bf-4900-b287-42bb4b212f61"/>
<skos:member rdf:resource="http://localhost:8000/4f98dedc-8477-49f8-b080-0d00ac33b706"/>
<skos:member rdf:resource="http://localhost:8000/4bf0d9a7-c43a-4fd2-94e0-a62c4e911994"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/2279136b-d040-4cfd-b136-b002c8131b5d">
<skos:member rdf:resource="http://localhost:8000/feb97305-7fb7-4d49-90ac-f46df334f903"/>
<skos:member rdf:resource="http://localhost:8000/39f0df93-1cac-4a3a-9c7c-306c517b4f74"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/0dbbe7c6-44f9-4e02-a20e-d47d4908cf2d"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/979f75ff-ae2a-476e-a831-0c596e25b1da">
<skos:member rdf:resource="http://localhost:8000/a82f0f57-3178-40a1-a384-040e48deb3bd"/>
<skos:member rdf:resource="http://localhost:8000/bec2c54f-ac52-4505-bbd7-c7ba4ffc1ccf"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/3f8a2a3a-89c6-403e-8ed4-4eae235f7d88"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5855d162-ca88-4ca9-857c-437970bf83c1"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/4ff62d98-b9bb-49b6-888f-40337d9f0513">
<skos:member rdf:resource="http://localhost:8000/cdf65893-e805-48ef-9113-81256fe00442"/>
<skos:member rdf:resource="http://localhost:8000/7161ad7a-7ed4-43f5-b354-3287b3835da2"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b5fcb992-54cf-4396-9c39-004d6bb99e26">
<skos:member rdf:resource="http://localhost:8000/00c62c81-19c0-45e0-9826-e20ccc3f8d9c"/>
<skos:member rdf:resource="http://localhost:8000/9127a332-a135-42c2-ae0f-9206fe48b601"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/0e51e6c6-f3e2-4149-bb55-518722f661f4"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/e46bccb3-9486-4f8a-a82f-11d61f242b52"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/987b7939-1637-4d45-bac8-39b92d2cc675">
<skos:member rdf:resource="http://localhost:8000/3c7bb43e-9edf-4237-a0da-583cf7c40ebe"/>
<skos:member rdf:resource="http://localhost:8000/9e216c2d-b7ca-4496-9d56-ef3627659e72"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/bdd88a82-235b-4abc-9978-a011d8733b5f">
<skos:member rdf:resource="http://localhost:8000/5a630c04-5bc9-41d2-99a3-0833a394ee19"/>
<skos:member rdf:resource="http://localhost:8000/67eb5efc-7621-462d-8857-307b6a56e4d5"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/51e9358b-0eca-4f9f-8945-ad094bbda992"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f87d86d7-173c-4dc4-99d3-bd41e25b0ab1">
<skos:member rdf:resource="http://localhost:8000/cd5accbc-5c8a-40b6-a47b-bf28e791292c"/>
<skos:member rdf:resource="http://localhost:8000/9ebf3275-bfd9-46a3-9fa0-ad83d1527b03"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/c0f2a333-74ff-4bd5-9892-7dc6d727c714">
<skos:member rdf:resource="http://localhost:8000/0a5c88fe-9b31-4b94-b0e1-48663f819b79"/>
<skos:member rdf:resource="http://localhost:8000/0ca8da7e-f13a-45f8-aef6-4fa68ce4c0ef"/>
<skos:member rdf:resource="http://localhost:8000/1c64bc4d-a403-4ff0-b579-ac5dbc880732"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/47fdddd4-badc-4729-bf1f-3de15dadfd3c"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/db26d10f-9add-4ddf-8e2d-1d4635d12179">
<skos:member rdf:resource="http://localhost:8000/5916b649-7d61-44a3-a09e-d31f6fe8035e"/>
<skos:member rdf:resource="http://localhost:8000/94176d85-c71b-49a4-a84c-1b9c0ad2c50b"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5fbcc9c8-b170-448e-a2b3-a4e3bf77bd4e"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/55a6d59d-a734-4f8b-8a89-13e30fbfcb6a">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5020eaab-730b-402c-ae80-05d369895cce"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/a5263356-5bba-4bde-843e-6922037050f8"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/22db7d50-833f-45f5-9478-332896c8cda8"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "c2bfa592-9938-40fa-8727-b5746d7fc76f", "value": "Overall condition"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/342dabd1-eb16-49d3-b062-e668a1af7614"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/2662a5d6-3512-44a3-8ce5-4d2509f56ae2"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/feb0a8c7-9e93-4434-b82c-1cc1f8343f2c"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/49ffba51-989a-4c6c-a797-f792b410234a">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/0ff8d8ec-ca55-4ace-8802-b209a62ba91f"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b6f398d1-1b81-4008-8bea-83dceda2cb2f"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/49e5ac10-47b7-4e4c-88df-9ae5c6d8924d"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/75392e20-daa5-45d6-9670-4df2366a81e1"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/890fb6dd-f9d9-421c-9320-dfaa1b3ed919"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "3736c2d3-c2aa-4e9d-9cb4-9a17d0909e80", "value": "Disturbance effect"}
</skos:prefLabel>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/2ef3d684-f7d6-4123-9a18-f607e3456e86">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/88b3261a-ae31-4be7-93b6-7b4d79da839e"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "e32fbda8-f4ba-4f49-83ca-1e39d18b02d0", "value": "Measurement unit"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/90fb3e63-0830-4f02-af0b-cb0fc74ea31c">
<skos:member rdf:resource="http://localhost:8000/41619316-c843-44e3-b095-c2be673e5c50"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b3d6f6e2-fd3b-4daa-a5fc-574836136389">
<skos:member rdf:resource="http://localhost:8000/75d1d53c-284e-4ec1-9f46-e0743338b3eb"/>
</skos:Concept>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/1303fe33-d99f-419e-b409-3746e322d5f5">
<skos:scopeNote xml:lang="en">
{"id": "dd14c449-1aad-42e1-afd3-fdaa856b3950", "value": "This refers to the Type node in the Actor resource model "}
</skos:scopeNote>
<skos:prefLabel xml:lang="en">
{"id": "172c5e91-e5c8-4c82-882e-a004b187d062", "value": "Actor Type"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/3e9cce6e-d803-45e3-ad58-a920d93f1ef4">
<skos:member rdf:resource="http://localhost:8000/15380712-84b7-4294-b538-ce53d06c6e5e"/>
<skos:member rdf:resource="http://localhost:8000/5150ec5c-e816-4421-94da-ffd0ab62074d"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/628a6291-ef96-49b1-8061-660c2fafff0a"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/869fb793-0c24-488b-b738-12372f694ae5"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/38b0a38b-b420-404b-abe0-f1beddad15a0"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/190077a4-8727-463a-9987-c8c8a282c2aa">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/0ee7827a-34f4-440c-8f73-0d11b1d8f170"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "aecab289-1f5c-4ab4-ac38-b958878a029c", "value": "Measurement type"}
</skos:prefLabel>
<skos:definition xml:lang="ar">
{"id": "19c8f703-7fd4-47f2-acb3-19dcbe73a0e5", "value": "\u0646\u0648\u0639 \u0627\u0644\u0642\u064a\u0627\u0633 \u0627\u0644\u0645\u0633\u062c\u0644 \u0641\u0649 \u0627\u0644\u0645\u0648\u0642\u0639 \u0627\u0644\u0627\u062b\u0631\u064a"}
</skos:definition>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/35f52226-2b59-4ebd-92fb-79c5d410ca91"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/4b0520d3-5a3a-4c20-9156-694e9f6e36a3"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/a612e7b3-c4d1-40a7-a761-0c44e0bffa8f"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/981a50d1-eab8-46cb-b86c-561e5f6f927a"/>
</skos:member>
<skos:prefLabel xml:lang="ar">
{"id": "fdb6f90a-e581-456b-a357-056e2ac98ebf", "value": "\u0646\u0648\u0639 \u0627\u0644\u0642\u064a\u0627\u0633"}
</skos:prefLabel>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/63bbc878-e7da-44e4-adcd-42cbf0993f22">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/254a24fc-e9ad-44be-bf78-5cf376d56dce"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/a3bf131e-54b5-40cf-ba0e-65a86036a604">
<skos:member rdf:resource="http://localhost:8000/022cd692-320f-4913-85d4-54d83abc7cb9"/>
<skos:member rdf:resource="http://localhost:8000/b4a95ce0-253e-47d6-ba9e-3b9e42da83f6"/>
<skos:member rdf:resource="http://localhost:8000/45d69b5f-3635-4fa9-802a-2d3e21ab224c"/>
</skos:Concept>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "1c64305f-3187-4e90-94c5-ee57596cfe0f", "value": "Remote sensing activity"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/6ca249ad-ea67-451d-ad16-769574201cc2">
<skos:member rdf:resource="http://localhost:8000/97d60f82-ab67-4987-aec4-e4daaf7803fb"/>
<skos:member rdf:resource="http://localhost:8000/4a2185af-f080-44d8-8977-e14ef3257b9a"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/a9ab33c1-9bd1-40f3-bc42-c644df9d9ee0">
<skos:member rdf:resource="http://localhost:8000/19319c1d-bf62-42d5-85dd-2223b1176106"/>
<skos:member rdf:resource="http://localhost:8000/965ece99-c369-4079-a9f6-d23e569057d3"/>
<skos:member rdf:resource="http://localhost:8000/a5819b44-8ba2-4bca-a3e7-2d66bc2a3843"/>
</skos:Concept>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/33cc174e-e513-49ae-81d5-c4afff854dc4">
<skos:prefLabel xml:lang="fr">
{"id": "eb90743f-f147-4d3b-9e9b-13bafe7df5d6", "value": "Certitude quant \u00e0 la fonction de site"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/2d9e358c-3386-4d7a-b5eb-d9ec2288bc5b"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/7ca3e187-06cb-4563-9561-3cc0d004be12"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/a6e2a504-5315-43e1-a9fc-334ec763989e"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "949bde4d-32a8-4c43-9c04-e73495cce0b5", "value": "Site function certainty"}
</skos:prefLabel>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/9c0300f7-3227-42b7-b39f-52597319ffec">
<skos:prefLabel xml:lang="fr">
{"id": "791eac05-fbb6-4034-905b-81fd2f84f666", "value": "Type de collecte"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5d145a54-2da6-4a9d-9fef-3c445090a1c9"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ff7b8306-59c1-4336-b937-0ff510e70804">
<skos:member rdf:resource="http://localhost:8000/a8dcc532-501d-406a-9097-ae20084c22e9"/>
<skos:member rdf:resource="http://localhost:8000/e70664f5-24cc-4264-86c6-2318c85db59e"/>
<skos:member rdf:resource="http://localhost:8000/cfdf2cd0-e300-451d-bd8d-e31f694f8f22"/>
<skos:member rdf:resource="http://localhost:8000/5546af07-5ca0-4129-a4a9-32b8cb74e9ba"/>
<skos:member rdf:resource="http://localhost:8000/fe0d72e8-59f7-4595-b7c0-7e99aa8563ab"/>
<skos:member rdf:resource="http://localhost:8000/3d307152-ac44-463f-b8c2-bdbb82a7aae9"/>
<skos:member rdf:resource="http://localhost:8000/0e6e3452-8a35-433c-ab61-96e1484eff05"/>
</skos:Concept>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "3077e54b-58dc-47c6-b3ba-34fcc2873628", "value": "Type of collection"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1c8684cd-7e57-4d91-ba90-fd4d1c1b986d"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ec215496-cb4f-463c-845d-dbf026e9dc8e"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/a4e1d411-a6b1-4e1d-aa5a-737eef14753f">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/c7f7084a-2ac6-4d15-9b3d-d3916856f948">
<skos:member rdf:resource="http://localhost:8000/1e5f43b8-16f2-493a-a9db-c05f07d33786"/>
<skos:member rdf:resource="http://localhost:8000/2e6fc20d-e2c8-4b23-b323-c1bb748e1895"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/bbda6a0b-57fc-4091-b557-4b771f665547"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/12cf44f8-f258-4a5d-97da-82d3b5700cd4"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ec9e8dc1-c10d-4b91-90bd-66e97d2e66d9">
<skos:member rdf:resource="http://localhost:8000/8f4c70f1-3b60-4422-b66c-b93f7b9fa374"/>
<skos:member rdf:resource="http://localhost:8000/1892d203-b0f0-43a8-aa86-79ad5b84521c"/>
<skos:member rdf:resource="http://localhost:8000/b5009028-35ee-4c59-8516-f234a66eab2b"/>
<skos:member rdf:resource="http://localhost:8000/895cb294-6c69-4c6d-b393-5c696b845c66"/>
<skos:member rdf:resource="http://localhost:8000/1c987769-7c27-4bb3-90d0-1875c1b88474"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f939d205-7461-410e-87b3-2e194b62f0f9">
<skos:member rdf:resource="http://localhost:8000/12694208-2acf-4926-abda-8dab0871825c"/>
<skos:member rdf:resource="http://localhost:8000/b9cabe77-846d-402d-adcd-bb43006c8c54"/>
<skos:member rdf:resource="http://localhost:8000/8d37d262-855d-4103-9fc4-149d04387af2"/>
<skos:member rdf:resource="http://localhost:8000/a80583a5-bc1a-447b-b65f-66d89a61dd86"/>
<skos:member rdf:resource="http://localhost:8000/1887cc2e-455d-4281-85d9-9c1e77a36753"/>
<skos:member rdf:resource="http://localhost:8000/1c1be75d-f6be-4b3b-b1b0-a5553c44f1d1"/>
<skos:member rdf:resource="http://localhost:8000/157b95ca-ebc3-4613-986a-0d4d9d65b299"/>
<skos:member rdf:resource="http://localhost:8000/c8dba5f0-ad0d-4e3c-8bd8-556f742812ec"/>
<skos:member rdf:resource="http://localhost:8000/368e2783-b30d-409e-a968-628ab11fa382"/>
<skos:member rdf:resource="http://localhost:8000/a56afeaf-88a4-4bd8-8d25-0c60799b2735"/>
<skos:member rdf:resource="http://localhost:8000/f0cc8546-00dc-4ec5-805e-c1319268d161"/>
<skos:member rdf:resource="http://localhost:8000/80506d62-00ee-44c7-870e-3ee8e2eee760"/>
<skos:member rdf:resource="http://localhost:8000/3d2b0c01-2271-44f0-9aae-21686468151b"/>
<skos:member rdf:resource="http://localhost:8000/72ddb6b0-c988-436a-881e-cfe0d452a5b0"/>
<skos:member rdf:resource="http://localhost:8000/94eb0738-3fc6-490f-935e-d04f0340daf2"/>
<skos:member rdf:resource="http://localhost:8000/0c57e100-3bdc-46bf-bde5-f8e0032cb51f"/>
<skos:member rdf:resource="http://localhost:8000/b72132bb-0730-472f-a5b5-faa322f0c4c9"/>
<skos:member rdf:resource="http://localhost:8000/446fbcf6-d052-47f9-946d-d1d62089cb78"/>
</skos:Concept>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "47e07386-c6ce-4211-934c-ae802ed6f7f6", "value": "Interpetation"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/68c27dc3-28a8-4fc3-80d5-cd88b3320534">
<skos:member rdf:resource="http://localhost:8000/f3941ff9-2629-486d-8c1b-763b3918c9b4"/>
<skos:member rdf:resource="http://localhost:8000/fec240f0-d862-4afa-8c80-ba4cbc3b077e"/>
<skos:member rdf:resource="http://localhost:8000/3e42067d-8665-4754-ac1b-2c081d762aec"/>
<skos:member rdf:resource="http://localhost:8000/21921d6a-2294-4a62-8357-97cae58b61a6"/>
<skos:member rdf:resource="http://localhost:8000/217c3bfe-5228-4077-983c-f32deb4482d1"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/0f23f194-3f52-4e44-bc8b-68180f02bb15">
<skos:member rdf:resource="http://localhost:8000/b67e95b8-6026-48b0-b590-c1487cbea440"/>
<skos:member rdf:resource="http://localhost:8000/dd231655-0a88-456a-bb9b-33b8cb58934d"/>
<skos:member rdf:resource="http://localhost:8000/f5d7305e-49e8-4c01-8188-442a8f75fabb"/>
<skos:member rdf:resource="http://localhost:8000/743c6434-4d37-4933-b82a-f3f1b8d62c22"/>
<skos:member rdf:resource="http://localhost:8000/9b3712d8-a7ae-47d1-bbce-8a9c283b00cf"/>
<skos:member rdf:resource="http://localhost:8000/07fb745c-b438-46bc-89e0-68e8fc53f7ba"/>
<skos:member rdf:resource="http://localhost:8000/485f3df6-aea1-47b3-9918-4e730342a95a"/>
<skos:member rdf:resource="http://localhost:8000/1387259a-4212-4125-837e-3d630c256acf"/>
<skos:member rdf:resource="http://localhost:8000/4158d4b9-69ba-44b5-8fd5-2295c9841633"/>
<skos:member rdf:resource="http://localhost:8000/188b53ce-4dca-46e4-897f-53cd4af0974f"/>
<skos:member rdf:resource="http://localhost:8000/0b092ac0-1c86-4e47-ad38-97ea6dab1716"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/3a5d28a3-cbf3-4be1-aa87-1841ee2e2ba1"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f455a9bf-a090-4d54-964e-272e9552b7f5">
<skos:member rdf:resource="http://localhost:8000/42d5b32a-72c0-46bf-9e55-489459c3846a"/>
<skos:member rdf:resource="http://localhost:8000/b439ad4f-8c25-46f2-b172-01fb8bfe7655"/>
<skos:member rdf:resource="http://localhost:8000/b47f60a6-8cc7-442e-8ed1-b0669c2b1092"/>
<skos:member rdf:resource="http://localhost:8000/d0a29430-71fd-4bae-b738-1af410244484"/>
<skos:member rdf:resource="http://localhost:8000/66fc41a6-d074-4861-92f7-4e807da12916"/>
<skos:member rdf:resource="http://localhost:8000/8ca05a2e-b409-46a7-841a-a78d485df7c8"/>
<skos:member rdf:resource="http://localhost:8000/5afb516b-d786-4a65-a7ee-a948777a9800"/>
<skos:member rdf:resource="http://localhost:8000/cbf5bedc-f2ef-4115-81e2-fb6426647d29"/>
<skos:member rdf:resource="http://localhost:8000/f8484f79-8448-49dd-9a39-ca309c32c1e5"/>
<skos:member rdf:resource="http://localhost:8000/d4425ec3-4b81-48d0-9118-b43a9751ea8b"/>
<skos:member rdf:resource="http://localhost:8000/04b3d830-f303-4834-9ae0-283c18d804c6"/>
<skos:member rdf:resource="http://localhost:8000/3e7ecfd2-0f7b-468f-a30d-2fb5b618c4f2"/>
<skos:member rdf:resource="http://localhost:8000/b7afe8e6-c7bb-480f-8dc4-52261d9810de"/>
<skos:member rdf:resource="http://localhost:8000/1bd690ec-effb-4e7e-9aa7-371cfdf98ab3"/>
<skos:member rdf:resource="http://localhost:8000/ed023080-40dc-4663-9686-69cb38e3552f"/>
<skos:member rdf:resource="http://localhost:8000/88bed6b7-8dfd-4e9e-833e-d96bc6f92595"/>
<skos:member rdf:resource="http://localhost:8000/a29d52be-ab11-440c-b247-51d5c28857ac"/>
<skos:member rdf:resource="http://localhost:8000/bba2d102-5ace-4aef-bba0-3924cc4cac77"/>
<skos:member rdf:resource="http://localhost:8000/60785b51-df13-403b-aa2d-f2df67192d13"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/4f08fbd1-cdaa-432f-9e14-8975aced9209"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/fd9cb0b9-e363-4751-89d5-0fd6ce9e2ac2">
<skos:member rdf:resource="http://localhost:8000/af6f14a8-c897-4abd-83ac-3ebc16601ed2"/>
<skos:member rdf:resource="http://localhost:8000/e2110219-da25-418f-b3e5-b11c64af99ae"/>
<skos:member rdf:resource="http://localhost:8000/89d64eac-4f8b-4012-8342-6bd538fae171"/>
<skos:member rdf:resource="http://localhost:8000/0bdf31e6-62d4-4b86-b099-076c5a4462ab"/>
<skos:member rdf:resource="http://localhost:8000/d741849b-d8fb-4009-a95a-29663697c814"/>
<skos:member rdf:resource="http://localhost:8000/57903a1e-bfa6-43df-a79f-289363d8d52c"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/c2a397ee-59fa-4178-a614-bdeffece0668">
<skos:member rdf:resource="http://localhost:8000/6212a41f-5a4a-4cd7-890e-84f8f17bc3cd"/>
<skos:member rdf:resource="http://localhost:8000/aa4b5ed1-75a1-41c3-9c15-02c52cc46026"/>
<skos:member rdf:resource="http://localhost:8000/3f261f40-9d5d-45cc-a1ae-c732516230f0"/>
<skos:member rdf:resource="http://localhost:8000/00f09747-091d-4358-90e3-750a259b756b"/>
<skos:member rdf:resource="http://localhost:8000/89236026-a521-41f8-ac9c-a8a2e066814b"/>
<skos:member rdf:resource="http://localhost:8000/509900ab-7d0c-4583-bae9-88c9d1f55b91"/>
</skos:Concept>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/5c7eb9fb-531e-4a81-9aac-efbfde2e7f24">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b2db3c98-bf22-410b-b07f-1e77b21aa227"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "cf15f5d6-1d11-4064-8443-830471e16329", "value": "Ground truthed"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/7f41eea0-7a80-4463-a75b-bb0ff8a740ac"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/49a9a737-0ec7-46e9-a5e2-485dce3b322a"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/974e2282-5a02-4c1e-8811-e5b9ef67a571">
<skos:prefLabel xml:lang="en">
{"id": "f7482669-88f4-4c07-b2cb-c8fdfce20c3d", "value": "Survey type"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/6781df3b-7d04-4a88-b403-618eea714d0c">
<skos:member rdf:resource="http://localhost:8000/07241e0f-ca32-4b81-b9e8-958e4caddc0f"/>
<skos:member rdf:resource="http://localhost:8000/3d06f467-f354-4dbe-9efd-8df3f8cef701"/>
<skos:member rdf:resource="http://localhost:8000/7d4e06f8-d7b6-45f8-b59a-000945d5f382"/>
<skos:member rdf:resource="http://localhost:8000/9eb72802-ebe9-45f0-8fa0-32c05a1ec4f6"/>
<skos:member rdf:resource="http://localhost:8000/3ca09c84-9ed5-4c12-8991-391d07e57395"/>
<skos:member rdf:resource="http://localhost:8000/821e04c4-87d4-40a6-acac-746415c367ed"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/abc3b788-5ae9-423b-9675-73202f5114b9">
<skos:member rdf:resource="http://localhost:8000/c40dc295-08ad-4e9a-85ac-e8aeafa15d69"/>
<skos:member rdf:resource="http://localhost:8000/5b057049-3a53-46df-baff-f90cabb1d92f"/>
<skos:member rdf:resource="http://localhost:8000/cd3a80a1-2033-4c3d-a265-22166233174f"/>
<skos:member rdf:resource="http://localhost:8000/90d53d57-7f49-455f-afa6-d8e59357dd48"/>
</skos:Concept>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/fe60ac34-2bf2-4a22-ac5a-f3c2436df847">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/488559c7-d890-42bb-9e59-b015bfc6c880"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "dc37b140-d62a-49dc-9602-18b646696de0", "value": "Threat level"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/cf630041-64d8-4e22-98f7-6827d6b854dc"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/da7f8320-ea54-47a9-87ef-30007a8da5e7"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/cbf67f7d-b3fc-4f25-89c3-63fae46e7402"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b745d649-222b-4496-83a3-51ae1cdaf454"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/9fe63f7d-23ee-4de7-9dbc-55e35f0e827d"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/a23c1e01-cd7c-467f-8db6-774079603dfa">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1675021c-1183-4635-8c4f-e1a084580ced"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f288732c-933a-48f3-b145-0ec817a29e57"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "b77b8310-e3f5-414d-9987-ae3a22337ffd", "value": "Threat severity"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b987bcae-7059-41e3-a257-13fb405d3ad5"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/42a2e1a7-233a-40f4-b7c4-78f35de7c1c8">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/e0a4c3e8-66ff-4a9b-93fc-9c1b2500bf3a"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "117361a7-106e-4e60-8895-7028b8847302", "value": "Interpretation certainty"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/6b57da05-79b6-4dd6-83b9-6f7818eccbcb"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/3e5cde16-65c9-41e1-ab2c-30573bd65580"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/282dd94f-c54c-4d63-a441-2183b6df5889">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/9e81a2ad-3d4a-46cd-b784-9e9af27aeb68">
<skos:member rdf:resource="http://localhost:8000/d7cebbf2-7939-45fb-8832-4eff086af898"/>
<skos:member rdf:resource="http://localhost:8000/b3d47c5f-e12b-46b3-b213-de00c0a7efd6"/>
<skos:member rdf:resource="http://localhost:8000/076bfc03-3e35-4f82-9fbf-a480da55d2ad"/>
<skos:member rdf:resource="http://localhost:8000/82767a95-8d9d-4861-8278-d62d2da7c465"/>
<skos:member rdf:resource="http://localhost:8000/885345f0-a5dd-4c64-bd91-2d8dc1486cb7"/>
<skos:member rdf:resource="http://localhost:8000/a347178b-f6ad-4b12-a6d0-6edeb57bba0a"/>
<skos:member rdf:resource="http://localhost:8000/f62eba76-5e7d-4815-9489-618db0b3fe1b"/>
<skos:member rdf:resource="http://localhost:8000/0e6d3562-48fb-4c12-b639-acc86a3b7762"/>
<skos:member rdf:resource="http://localhost:8000/30e18a63-67b5-4def-9ab0-5b3773ba22ff"/>
<skos:member rdf:resource="http://localhost:8000/45312430-2596-463f-aa79-628644791436"/>
<skos:member rdf:resource="http://localhost:8000/d64eb7ef-2ffa-47fe-b13b-92b1284c009f"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f75c6bab-daa1-47e0-8679-94c00cb59737">
<skos:member rdf:resource="http://localhost:8000/43f751fb-2cbe-4970-9e3c-21d6d33e935a"/>
<skos:member rdf:resource="http://localhost:8000/e4c0153f-bbca-41c2-9d5c-3f8902297d87"/>
<skos:member rdf:resource="http://localhost:8000/daf23c0f-8c2d-4408-9cb2-697f528b6a87"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/067b6842-7620-4782-a592-f2ff6e195f3b">
<skos:member rdf:resource="http://localhost:8000/4bc601fa-5b1b-4446-a46c-513e5c1cd7dd"/>
<skos:member rdf:resource="http://localhost:8000/9e323767-98eb-40e0-a928-5c5ab5987d65"/>
<skos:member rdf:resource="http://localhost:8000/0c1ee567-9de6-44fb-8274-ffc487e017ef"/>
<skos:member rdf:resource="http://localhost:8000/828ccf17-d341-4985-91b4-4b90f4cdf97c"/>
<skos:member rdf:resource="http://localhost:8000/12e805e4-e5e9-4166-b6d2-071754603671"/>
<skos:member rdf:resource="http://localhost:8000/ebc9eab4-fa03-4315-b163-05f3dc995d1f"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/465cc2f1-b195-44e5-9e73-e215d77b3cb0">
<skos:member rdf:resource="http://localhost:8000/a286f000-bcc0-45d2-9cea-41ddafb19e55"/>
<skos:member rdf:resource="http://localhost:8000/2b24ad46-a388-47f6-bae1-1b1c41f80815"/>
<skos:member rdf:resource="http://localhost:8000/e493e64e-e40e-4311-a361-b5f42f849299"/>
<skos:member rdf:resource="http://localhost:8000/a69c5df6-7737-4f87-ad32-95ca8415c642"/>
<skos:member rdf:resource="http://localhost:8000/1ed066c4-b5dd-44e1-bbf2-407b2add60ed"/>
<skos:member rdf:resource="http://localhost:8000/b5ce32bb-1394-4704-adaf-91fb94fd2b76"/>
<skos:member rdf:resource="http://localhost:8000/5ab46ba0-ae30-4f8e-ab64-0b124dbfcb49"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/a2cdec53-b649-42f0-9f8b-938e07903f69">
<skos:member rdf:resource="http://localhost:8000/d09226f1-79ca-4449-820a-b7d6032ab877"/>
<skos:member rdf:resource="http://localhost:8000/47a5426d-b0d4-4007-a695-74363f105850"/>
<skos:member rdf:resource="http://localhost:8000/6b50829b-6973-47e7-a803-2752cf9b1a32"/>
<skos:member rdf:resource="http://localhost:8000/d0e1dc98-9071-4b8e-98bb-f15ccec09710"/>
<skos:member rdf:resource="http://localhost:8000/79034bb0-a41a-4470-8403-697c3c3d04b0"/>
<skos:member rdf:resource="http://localhost:8000/5de60a3c-a9e3-47ce-9640-1735c8c4aacc"/>
<skos:member rdf:resource="http://localhost:8000/c84459db-07c4-4854-bfb4-792e24bafbd2"/>
<skos:member rdf:resource="http://localhost:8000/e8ea2e55-1862-42d2-97eb-1be25acc91d3"/>
<skos:member rdf:resource="http://localhost:8000/4e7fe55e-260b-4f9b-ad3b-537748e5f47d"/>
<skos:member rdf:resource="http://localhost:8000/134a70cd-7848-474e-96dd-422f896b6fcc"/>
<skos:member rdf:resource="http://localhost:8000/a3384bf1-5954-4c48-b390-8b5cdb7484af"/>
<skos:member rdf:resource="http://localhost:8000/73bdd657-a00e-415c-8f8e-fd698bfcc5ae"/>
<skos:member rdf:resource="http://localhost:8000/4a432393-026a-42a9-972a-45077f8ab14b"/>
<skos:member rdf:resource="http://localhost:8000/8d69b941-b662-4235-8671-289f5b444847"/>
<skos:member rdf:resource="http://localhost:8000/ac0232b4-7064-4790-9d04-4d4ee114bd72"/>
<skos:member rdf:resource="http://localhost:8000/e7e63c6b-700e-4000-9244-917c8e9f772f"/>
</skos:Concept>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f103c42d-c5fd-43d8-ae21-6d78cdb8c61a"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/9e346420-fa6a-41ad-8c28-a3d75f56c5f6">
<skos:member rdf:resource="http://localhost:8000/5b5a564b-d097-47b0-aeaa-e1ae96cfd836"/>
<skos:member rdf:resource="http://localhost:8000/4475cecb-bf00-4c3f-b95d-90609a9ea7c5"/>
<skos:member rdf:resource="http://localhost:8000/1dba5d44-47a8-4441-a765-8a7ec318a857"/>
<skos:member rdf:resource="http://localhost:8000/3e60ffca-3232-4e4a-9870-ca55e2e19961"/>
<skos:member rdf:resource="http://localhost:8000/1feb0775-8c38-4fab-b452-fe88103f6d34"/>
<skos:member rdf:resource="http://localhost:8000/c2d07737-82f5-42c7-b38a-f6ef6383917b"/>
<skos:member rdf:resource="http://localhost:8000/7d021a36-ae9e-40d0-bc9e-35484dec6394"/>
<skos:member rdf:resource="http://localhost:8000/ec593907-d1de-4d94-ae21-92f7d54d88be"/>
</skos:Concept>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "151daee3-8f3a-455a-80d7-fd0076983957", "value": "Evidence"}
</skos:prefLabel>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/c9bb2f3f-b5d4-4ba8-9318-87772072dc2f">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/8a9979ac-d9b2-4b07-acea-ef34f03b9e35"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/941ab2d3-1919-4c50-b521-26375112e499"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "e84d0ceb-9cbd-4396-bad1-6908f60eacf1", "value": "Imagery analysis method"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/82297a44-18cf-4ac1-aaa2-c5396e1c3141"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b2d34407-238e-4a3b-ac96-19b73ca26440"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/d4d6cd1c-6467-4027-9663-61483060cb11"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f0210d2c-3451-4173-a536-5e96980e3af8"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/d4c98f02-85b2-4966-abbb-2ad9f00d74d3"/>
</skos:member>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/e8fc849a-cad3-49e1-852e-d76b7c32c5d0">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b5137eb3-5c02-4a90-8b7f-79b8918ede9b"/>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "1e32c011-915f-4550-adf9-7a2532a50ea4", "value": "Name type"}
</skos:prefLabel>
<skos:definition xml:lang="en">
{"id": "cf234ea0-997d-4477-ab3e-6c38649bd2fd", "value": "This is the name type for all the resource models "}
</skos:definition>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1e7b6051-391a-46d1-8b3e-411a79669d85"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/0da6ca1a-7148-4960-b02b-f87384c71993"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5ebd11de-cd0c-459e-9e7a-64382488af9e"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/441bf354-e558-4a9e-8dfb-615103779bc8"/>
</skos:member>
<skos:prefLabel xml:lang="fr">
{"id": "8971581f-6e84-4aec-bebc-4eafdefc3e61", "value": "Type du nom"}
</skos:prefLabel>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/a34fa9ec-e9ac-44b4-b313-451d91a5a82d">
<skos:altLabel xml:lang="en">
{"id": "d5d9db41-8310-4c23-88f1-8dd39bf93eb7", "value": "Sewer"}
</skos:altLabel>
</skos:Collection>
<skos:Collection rdf:about="http://localhost:8000/c4c82c5e-5253-48b0-8470-fdc5d5b3c2b7">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/7ab311e6-54c6-4cf3-a293-a5c822d3cf8d">
<skos:member rdf:resource="http://localhost:8000/24d0f48f-e8c6-43cf-8468-e6cd7661090f"/>
<skos:member rdf:resource="http://localhost:8000/ffe4f51a-c04b-4f24-9b2a-45a135217635"/>
<skos:member rdf:resource="http://localhost:8000/c3b1415f-36e9-4251-9fab-092b69e66047"/>
<skos:member rdf:resource="http://localhost:8000/82dde12e-90b7-4967-b8e6-d321785b330d"/>
<skos:member rdf:resource="http://localhost:8000/fdc586c3-a44b-4142-ad56-c208fb4b4999"/>
<skos:member rdf:resource="http://localhost:8000/f5a181e7-db75-46f8-9a95-fafb596c7a08"/>
<skos:member rdf:resource="http://localhost:8000/ae7ccda7-ad32-420b-b8c0-3a7b2f7dba3f"/>
<skos:member rdf:resource="http://localhost:8000/3be2fe8a-6cfe-4c57-bb9d-ceed68670691"/>
<skos:member rdf:resource="http://localhost:8000/1058f367-a545-407c-a335-5248ed3e8048"/>
<skos:member rdf:resource="http://localhost:8000/e1419bea-183f-4d0f-997d-b3e394d851f4"/>
<skos:member rdf:resource="http://localhost:8000/3115a3ed-f42d-48e1-a19d-df61879eec0d"/>
<skos:member rdf:resource="http://localhost:8000/c463d316-7b5f-4e38-8e84-b06ae23cd61a"/>
<skos:member rdf:resource="http://localhost:8000/318846e4-3073-4e8f-9b1d-42d30a9eda03"/>
<skos:member rdf:resource="http://localhost:8000/037f5c10-3eb0-4325-b625-b8b6eabd4e5b"/>
<skos:member rdf:resource="http://localhost:8000/77c74570-2676-4d06-a439-7ef102259d40"/>
<skos:member rdf:resource="http://localhost:8000/4adf58f1-387b-4445-977c-953447b3ed97"/>
<skos:member rdf:resource="http://localhost:8000/56d91dc9-7ad7-439f-806f-1d6bccd2bf91"/>
<skos:member rdf:resource="http://localhost:8000/11c57d99-eedf-4156-984a-aa82e197a568"/>
<skos:member rdf:resource="http://localhost:8000/52f75a1d-a1f3-4bdd-a54e-9ff71fd05c7b"/>
<skos:member rdf:resource="http://localhost:8000/63935552-afe7-4f80-b71d-871e505ca10b"/>
<skos:member rdf:resource="http://localhost:8000/a30668f2-1ec8-4faa-849f-ffd2dd9448b4"/>
<skos:member rdf:resource="http://localhost:8000/d3bbc701-d42f-400d-8825-16691e8ceb4e"/>
<skos:member rdf:resource="http://localhost:8000/ea530621-de16-4703-a9ac-4840d700c7ab"/>
</skos:Concept>
</skos:member>
<skos:prefLabel xml:lang="en">
{"id": "2ded507d-ff2f-449c-b9c1-68e607a48a00", "value": "Possible threat type"}
</skos:prefLabel>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/761f93ef-aa9b-4c10-9965-22f8a62810ac">
<skos:member rdf:resource="http://localhost:8000/c2ec3f83-8b4f-42b2-8d48-9c271bec37b2"/>
<skos:member rdf:resource="http://localhost:8000/7d2b2877-54ce-44a0-9f5a-b5acb5c79a4f"/>
<skos:member rdf:resource="http://localhost:8000/18593e61-439f-463a-bb88-bb2227f202db"/>
<skos:member rdf:resource="http://localhost:8000/b20135e5-83dd-4e9b-9ca8-2113a34ecb12"/>
<skos:member rdf:resource="http://localhost:8000/189caeb8-69a2-4c7e-9d95-c3043c376e2b"/>
<skos:member rdf:resource="http://localhost:8000/68decd18-3277-469f-b2f0-ab8f30b984c1"/>
<skos:member rdf:resource="http://localhost:8000/ba6b5b79-47df-4441-8037-ce7d0b7d58fe"/>
<skos:member rdf:resource="http://localhost:8000/4de08727-2be7-4b4d-bdb8-f29f4a86fe61"/>
<skos:member rdf:resource="http://localhost:8000/f414e642-754b-44e4-bd58-7298eac88b9a"/>
<skos:member rdf:resource="http://localhost:8000/fef3c640-c464-44c0-a032-c3ddf9ee584f"/>
<skos:member rdf:resource="http://localhost:8000/7782f089-da7c-4f62-becd-7545615568f9"/>
<skos:member rdf:resource="http://localhost:8000/4f898db1-c2ee-4360-8b6c-75eb0e5269d0"/>
</skos:Concept>
</skos:member>
</skos:Collection>
<skos:Concept rdf:about="http://localhost:8000/1feb0775-8c38-4fab-b452-fe88103f6d34"/>
<skos:Concept rdf:about="http://localhost:8000/1c987769-7c27-4bb3-90d0-1875c1b88474"/>
<skos:Concept rdf:about="http://localhost:8000/25de39cd-1250-48c0-8aa7-f7d5f1e5bbe2"/>
<skos:Concept rdf:about="http://localhost:8000/e46ea77b-b791-4ca9-a891-f15cc7813ae3"/>
<skos:Concept rdf:about="http://localhost:8000/485f3df6-aea1-47b3-9918-4e730342a95a"/>
<skos:Concept rdf:about="http://localhost:8000/4adf58f1-387b-4445-977c-953447b3ed97"/>
<skos:Concept rdf:about="http://localhost:8000/189caeb8-69a2-4c7e-9d95-c3043c376e2b">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5829b4ba-2b77-4904-ae05-3d2b21873112"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/fd7b72a0-5500-4ebe-8101-70c70a2a922d"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1cba1685-50fd-4286-81b8-b95f7fda1728"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/c99e0aa4-ef70-4235-8f2d-7ab1ede7290c"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/fc2e2bc2-3289-43c6-9007-3aee7ed4684c"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/f8484f79-8448-49dd-9a39-ca309c32c1e5"/>
<skos:Concept rdf:about="http://localhost:8000/fd9e102e-453f-43f2-965b-4e8e237cfd25"/>
<skos:Concept rdf:about="http://localhost:8000/a6a150db-67b2-4dd2-bc51-651a7c512009"/>
<skos:Concept rdf:about="http://localhost:8000/821e04c4-87d4-40a6-acac-746415c367ed">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1a4c3152-a6d7-486c-a4ef-227f2bdf3fe4"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/6733aab3-1775-4b61-a8e1-9201d295172d"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/9ba37735-fc85-41cf-8aca-efaaeeac7540"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/995cae0e-7043-478e-88d6-1894e9b56fd4"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/2e92a0d3-bbbb-418e-8c05-3bebbbfe49b9"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/fa045cbd-2425-4468-b23c-b364d9218a91"/>
<skos:Concept rdf:about="http://localhost:8000/18593e61-439f-463a-bb88-bb2227f202db">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/db13542c-2834-4a7d-8a72-855dafc95999"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/d216fab0-12da-49f2-94bc-6523d68a99b7"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/d741849b-d8fb-4009-a95a-29663697c814"/>
<skos:Concept rdf:about="http://localhost:8000/e7e63c6b-700e-4000-9244-917c8e9f772f"/>
<skos:Concept rdf:about="http://localhost:8000/1058f367-a545-407c-a335-5248ed3e8048"/>
<skos:Concept rdf:about="http://localhost:8000/1c1be75d-f6be-4b3b-b1b0-a5553c44f1d1"/>
<skos:Concept rdf:about="http://localhost:8000/3b87ef5b-3236-41f6-8f73-dcf033ba40d8"/>
<skos:Concept rdf:about="http://localhost:8000/32d03b98-d4d5-46bb-9152-2b401a9e92bb"/>
<skos:Concept rdf:about="http://localhost:8000/22ee00ba-cd80-4b3d-9367-141be24a2f16"/>
<skos:Concept rdf:about="http://localhost:8000/872dcd85-bf07-44ca-a2c5-d458ce3ef97c"/>
<skos:Concept rdf:about="http://localhost:8000/af6f14a8-c897-4abd-83ac-3ebc16601ed2"/>
<skos:Concept rdf:about="http://localhost:8000/b245a11b-cf7e-4b1d-9d37-6ee86d859f3f"/>
<skos:Concept rdf:about="http://localhost:8000/42d5b32a-72c0-46bf-9e55-489459c3846a"/>
<skos:Concept rdf:about="http://localhost:8000/ebc9eab4-fa03-4315-b163-05f3dc995d1f"/>
<skos:Concept rdf:about="http://localhost:8000/97d60f82-ab67-4987-aec4-e4daaf7803fb">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/74884869-1126-4df5-a51d-7570d6782f05"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/cdb590fd-db76-4d25-898f-0d2aa47043d4"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f0a067c3-cb0b-4b80-8c5b-3921bcd8a70c"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/01b5458c-cb49-4da7-a7c8-a3213900fb30"/>
<skos:Concept rdf:about="http://localhost:8000/d7cebbf2-7939-45fb-8832-4eff086af898">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/8763bb3c-77a1-477d-a2b2-1534a2bf7383"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/6f8a84c1-0f29-4442-874f-1cba425ebe65"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/d1645f61-c3a0-499e-bed8-8e609cc00037"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/19c7c307-8f0d-49a9-a51c-e98e09a1bb7a"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/2873de84-930b-4164-94d0-b70c43796e57"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/a30b7634-4691-4581-b05e-5bd0a0a33da3"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b7cb5666-0277-4ea7-ac9b-9b23ee297327"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/e3705b8b-7d25-4ef5-9235-beda23c5c6b5"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/1887cc2e-455d-4281-85d9-9c1e77a36753">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/23f51e78-b53e-4949-ab16-34ea664c9f4f"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/62aba907-0741-42e4-8859-a8705c33dab5"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/10a995da-fbf0-48cc-8de4-9b2446eed5e8"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/3f26088b-350e-4223-b39c-a33ae4f586c7"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/268aaaf9-a7f0-46c4-a6b8-b90da85eed13"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/418a6c01-6187-44a1-9b7f-934b710fe0eb"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/d4082979-9f94-4596-a8ed-b339864f3181"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/a2cecb21-eae5-4365-89b5-594f94a8e654"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/5b5a564b-d097-47b0-aeaa-e1ae96cfd836"/>
<skos:Concept rdf:about="http://localhost:8000/cfdf2cd0-e300-451d-bd8d-e31f694f8f22"/>
<skos:Concept rdf:about="http://localhost:8000/a56afeaf-88a4-4bd8-8d25-0c60799b2735"/>
<skos:Concept rdf:about="http://localhost:8000/73bdd657-a00e-415c-8f8e-fd698bfcc5ae"/>
<skos:Concept rdf:about="http://localhost:8000/b5ce32bb-1394-4704-adaf-91fb94fd2b76"/>
<skos:Concept rdf:about="http://localhost:8000/85689c7a-9dc8-46ae-a7c4-feb3fd2edc38"/>
<skos:Concept rdf:about="http://localhost:8000/89f9e471-c574-40d2-882c-fab9d6f37b8b"/>
<skos:Concept rdf:about="http://localhost:8000/45d69b5f-3635-4fa9-802a-2d3e21ab224c">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/03230d65-f31e-45dd-a0fc-9a29e097013e"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/0960bea4-b183-47b5-aa55-41fc7398e179"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/c339c7c6-a25b-4df9-a134-3378f2db5907"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/c0769f6e-209b-45b0-bd75-21a73b032a95"/>
<skos:Concept rdf:about="http://localhost:8000/56d91dc9-7ad7-439f-806f-1d6bccd2bf91"/>
<skos:Concept rdf:about="http://localhost:8000/5546af07-5ca0-4129-a4a9-32b8cb74e9ba"/>
<skos:Concept rdf:about="http://localhost:8000/188b53ce-4dca-46e4-897f-53cd4af0974f"/>
<skos:Concept rdf:about="http://localhost:8000/63935552-afe7-4f80-b71d-871e505ca10b">
<skos:member rdf:resource="http://localhost:8000/3b87ef5b-3236-41f6-8f73-dcf033ba40d8"/>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/a4548e7e-e1c2-4170-9284-1087d3335a8e"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/445c1818-a0dc-4be4-8328-1abb78413353"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b2ca6379-1693-4c46-aabd-2f1a5395cafb"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/e493e64e-e40e-4311-a361-b5f42f849299"/>
<skos:Concept rdf:about="http://localhost:8000/aa4b5ed1-75a1-41c3-9c15-02c52cc46026"/>
<skos:Concept rdf:about="http://localhost:8000/07fb745c-b438-46bc-89e0-68e8fc53f7ba"/>
<skos:Concept rdf:about="http://localhost:8000/e70664f5-24cc-4264-86c6-2318c85db59e"/>
<skos:Concept rdf:about="http://localhost:8000/89236026-a521-41f8-ac9c-a8a2e066814b"/>
<skos:Concept rdf:about="http://localhost:8000/d18fe978-60f2-462f-a6dc-b3fc6e310352">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/abc83a27-d0c5-4c82-83f4-41b36099086b"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/4a58287e-1414-4c00-890b-e1df9ad5d57b"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/46f02d2e-0218-47a4-8a01-16523b213e17"/>
<skos:Concept rdf:about="http://localhost:8000/feb97305-7fb7-4d49-90ac-f46df334f903"/>
<skos:Concept rdf:about="http://localhost:8000/509900ab-7d0c-4583-bae9-88c9d1f55b91"/>
<skos:Concept rdf:about="http://localhost:8000/c84459db-07c4-4854-bfb4-792e24bafbd2"/>
<skos:Concept rdf:about="http://localhost:8000/d64eb7ef-2ffa-47fe-b13b-92b1284c009f">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/6cbe0979-a1dc-47dd-86c8-97a8fdc23bf5"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/3e651be5-2ac5-4ee2-afaf-9711e37b20fe"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/3103efe4-341f-446c-bba1-f0e68236cfd2"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/1b0b8e08-c4ac-496e-8db0-1adf02bbd5cc"/>
<skos:Concept rdf:about="http://localhost:8000/c40dc295-08ad-4e9a-85ac-e8aeafa15d69"/>
<skos:Concept rdf:about="http://localhost:8000/d0e1dc98-9071-4b8e-98bb-f15ccec09710"/>
<skos:Concept rdf:about="http://localhost:8000/c2d07737-82f5-42c7-b38a-f6ef6383917b"/>
<skos:Concept rdf:about="http://localhost:8000/0b092ac0-1c86-4e47-ad38-97ea6dab1716"/>
<skos:Concept rdf:about="http://localhost:8000/6218920a-0e7e-48a5-9698-e7b88e664f47"/>
<skos:Concept rdf:about="http://localhost:8000/7f0d45e4-598e-4f52-b0ca-ac3dc9403008"/>
<skos:Concept rdf:about="http://localhost:8000/1892d203-b0f0-43a8-aa86-79ad5b84521c"/>
<skos:Concept rdf:about="http://localhost:8000/5afb516b-d786-4a65-a7ee-a948777a9800"/>
<skos:Concept rdf:about="http://localhost:8000/04b3d830-f303-4834-9ae0-283c18d804c6"/>
<skos:Concept rdf:about="http://localhost:8000/3a90e5da-7dd2-4532-ac40-3186605c8068"/>
<skos:Concept rdf:about="http://localhost:8000/446fbcf6-d052-47f9-946d-d1d62089cb78"/>
<skos:Concept rdf:about="http://localhost:8000/48aa8413-1ea2-416f-966c-de5c2bd3f249">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1ffd169c-2cd3-4432-bfe3-11f24deaa529"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/0c9e2529-5e63-4b9e-b1b2-d1d866b92705"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/00da5128-ef4e-4a0a-b6ae-48108ba8e3e6"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1e0cd53c-17cb-4739-996d-aca376f59322"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/0c4000a8-5034-420b-a97b-d8915d773611"/>
<skos:Concept rdf:about="http://localhost:8000/885345f0-a5dd-4c64-bd91-2d8dc1486cb7"/>
<skos:Concept rdf:about="http://localhost:8000/19319c1d-bf62-42d5-85dd-2223b1176106"/>
<skos:Concept rdf:about="http://localhost:8000/b3d47c5f-e12b-46b3-b213-de00c0a7efd6">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/7eab520e-3a97-4eac-9057-bdf4e8950d0d"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/2b1d5702-5f07-455a-bd6e-5833baea3ea3">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/e807e7d0-5df5-4873-84d5-e516fd339dd5"/>
</skos:member>
<skos:member rdf:resource="http://localhost:8000/46f02d2e-0218-47a4-8a01-16523b213e17"/>
<skos:member rdf:resource="http://localhost:8000/fa045cbd-2425-4468-b23c-b364d9218a91"/>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/69d14fb4-be3c-4603-bd0c-0a8975ac890e"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/87245fe4-812f-4dc2-8b9d-c1ea87867478"/>
<skos:Concept rdf:about="http://localhost:8000/828ccf17-d341-4985-91b4-4b90f4cdf97c">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/be15fa6c-e3c3-47ca-a378-e3cd682a311f"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/ed023080-40dc-4663-9686-69cb38e3552f"/>
<skos:Concept rdf:about="http://localhost:8000/ec593907-d1de-4d94-ae21-92f7d54d88be"/>
<skos:Concept rdf:about="http://localhost:8000/ad2fbfbd-bde0-4587-a55a-d8937c86a715"/>
<skos:Concept rdf:about="http://localhost:8000/68decd18-3277-469f-b2f0-ab8f30b984c1">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/4bed44dc-203e-4690-a7c5-06c405a61ca0"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/fa3012ff-f998-43d9-8098-3102a7bccee9"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ec1d6664-2cd1-4b0e-a64f-91c94665221c"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/7f0da314-edc5-49b2-8032-62ad6f6bc24e"/>
<skos:Concept rdf:about="http://localhost:8000/5a630c04-5bc9-41d2-99a3-0833a394ee19"/>
<skos:Concept rdf:about="http://localhost:8000/66559377-2317-40f4-958a-50e886cdf934"/>
<skos:Concept rdf:about="http://localhost:8000/f62eba76-5e7d-4815-9489-618db0b3fe1b"/>
<skos:Concept rdf:about="http://localhost:8000/c2ec3f83-8b4f-42b2-8d48-9c271bec37b2"/>
<skos:Concept rdf:about="http://localhost:8000/6b50829b-6973-47e7-a803-2752cf9b1a32"/>
<skos:Concept rdf:about="http://localhost:8000/6c1a0784-d6de-44c2-b4dc-b5ee984a4a7c"/>
<skos:Concept rdf:about="http://localhost:8000/4e7fe55e-260b-4f9b-ad3b-537748e5f47d"/>
<skos:Concept rdf:about="http://localhost:8000/45312430-2596-463f-aa79-628644791436"/>
<skos:Concept rdf:about="http://localhost:8000/a5819b44-8ba2-4bca-a3e7-2d66bc2a3843">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/27bd12ef-f0a3-4ae8-ae40-e9df1cb2d9d6"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/55c12e61-8994-4614-b68d-c59b97f89ec4"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/88ab9756-45b7-4dfb-8d60-523c21a3628f"/>
<skos:Concept rdf:about="http://localhost:8000/e8ea2e55-1862-42d2-97eb-1be25acc91d3"/>
<skos:Concept rdf:about="http://localhost:8000/3b103375-739a-4307-885f-0aeb47484a69"/>
<skos:Concept rdf:about="http://localhost:8000/12050340-ef4b-499a-aa36-5b5783e255d8">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/f21621b6-6143-4a54-acf1-8a5ed067186e"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/697decc7-c074-413f-99f6-771284ddfbbc"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/409d45d6-15d9-44df-84f7-9c74cef3e983"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/5de60a3c-a9e3-47ce-9640-1735c8c4aacc"/>
<skos:Concept rdf:about="http://localhost:8000/b67e95b8-6026-48b0-b590-c1487cbea440"/>
<skos:Concept rdf:about="http://localhost:8000/4bc601fa-5b1b-4446-a46c-513e5c1cd7dd"/>
<skos:Concept rdf:about="http://localhost:8000/bec2c54f-ac52-4505-bbd7-c7ba4ffc1ccf"/>
<skos:Concept rdf:about="http://localhost:8000/00c62c81-19c0-45e0-9826-e20ccc3f8d9c"/>
<skos:Concept rdf:about="http://localhost:8000/67eb5efc-7621-462d-8857-307b6a56e4d5"/>
<skos:Concept rdf:about="http://localhost:8000/6ffc7e2e-088f-49cc-a71e-35452b341ee9">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/5bffbc75-b2c2-4177-a2a9-94bf357fc592"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b8241ea1-eca5-4609-a6fe-9cabbbbb7a5f"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/59e1c331-0f10-4eeb-913c-204f4819f31c"/>
<skos:Concept rdf:about="http://localhost:8000/fdbaee06-b330-4ed8-9b7c-07c6aaf8f0bb"/>
<skos:Concept rdf:about="http://localhost:8000/f1812ea4-a815-4a88-adfa-d72d08606354"/>
<skos:Concept rdf:about="http://localhost:8000/5cfa5852-06ca-44b5-9969-2bb1157bec01"/>
<skos:Concept rdf:about="http://localhost:8000/a80583a5-bc1a-447b-b65f-66d89a61dd86"/>
<skos:Concept rdf:about="http://localhost:8000/6212a41f-5a4a-4cd7-890e-84f8f17bc3cd"/>
<skos:Concept rdf:about="http://localhost:8000/43f751fb-2cbe-4970-9e3c-21d6d33e935a"/>
<skos:Concept rdf:about="http://localhost:8000/a47027fb-0f2e-4ac4-a9ee-bfd88756b670"/>
<skos:Concept rdf:about="http://localhost:8000/0e6e3452-8a35-433c-ab61-96e1484eff05"/>
<skos:Concept rdf:about="http://localhost:8000/b20135e5-83dd-4e9b-9ca8-2113a34ecb12">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/9288a670-9ef9-4f72-8a71-98043c1a5075"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/875aaa26-0369-4144-a2cd-38d40a681a59"/>
</skos:member>
<skos:member rdf:resource="http://localhost:8000/3a90e5da-7dd2-4532-ac40-3186605c8068"/>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/dcdc8a03-9ac5-479b-a778-5730d471d3b0"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/e015dd5c-9f25-4bf3-b13a-c55b1abf4737"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/ca144b17-4b3e-4e2d-aa43-ae0cd70a4f06"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/a9639b7a-dd25-41e9-8ed0-ed5820dec17a"/>
<skos:Concept rdf:about="http://localhost:8000/0bdf31e6-62d4-4b86-b099-076c5a4462ab"/>
<skos:Concept rdf:about="http://localhost:8000/758e60a5-01c3-4232-9f9b-2e9870f75429"/>
<skos:Concept rdf:about="http://localhost:8000/a3384bf1-5954-4c48-b390-8b5cdb7484af"/>
<skos:Concept rdf:about="http://localhost:8000/3c9bea82-eea0-49f8-a521-90fdb6d2e3a3"/>
<skos:Concept rdf:about="http://localhost:8000/41619316-c843-44e3-b095-c2be673e5c50"/>
<skos:Concept rdf:about="http://localhost:8000/e2110219-da25-418f-b3e5-b11c64af99ae">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/0d03df7a-1181-46fe-aa1e-1d485913cf7d"/>
</skos:member>
<skos:member rdf:resource="http://localhost:8000/59e1c331-0f10-4eeb-913c-204f4819f31c"/>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/c8dba5f0-ad0d-4e3c-8bd8-556f742812ec"/>
<skos:Concept rdf:about="http://localhost:8000/011734b7-a0f6-44e9-acd5-57ff9e453be8"/>
<skos:Concept rdf:about="http://localhost:8000/a347178b-f6ad-4b12-a6d0-6edeb57bba0a">
<skos:member rdf:resource="http://localhost:8000/7f0da314-edc5-49b2-8032-62ad6f6bc24e"/>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/29c14a1a-68f0-4bdc-b345-e8a2f26fbda5"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/47cf2463-df9d-48ea-8021-3a6f2e586306"/>
<skos:Concept rdf:about="http://localhost:8000/12e805e4-e5e9-4166-b6d2-071754603671"/>
<skos:Concept rdf:about="http://localhost:8000/c463d316-7b5f-4e38-8e84-b06ae23cd61a"/>
<skos:Concept rdf:about="http://localhost:8000/5916b649-7d61-44a3-a09e-d31f6fe8035e"/>
<skos:Concept rdf:about="http://localhost:8000/a30668f2-1ec8-4faa-849f-ffd2dd9448b4"/>
<skos:Concept rdf:about="http://localhost:8000/1ed066c4-b5dd-44e1-bbf2-407b2add60ed"/>
<skos:Concept rdf:about="http://localhost:8000/ae7ccda7-ad32-420b-b8c0-3a7b2f7dba3f"/>
<skos:Concept rdf:about="http://localhost:8000/2a8db864-9484-4c30-af80-7de4118e396a">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/e651d038-c34a-407c-9a1b-84d713b3cf61"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/a8035926-0fd6-4052-90a5-d67ed015caea"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/107061df-6a07-47ef-9d4e-265e28132cbe"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/ea530621-de16-4703-a9ac-4840d700c7ab"/>
<skos:Concept rdf:about="http://localhost:8000/ac0232b4-7064-4790-9d04-4d4ee114bd72"/>
<skos:Concept rdf:about="http://localhost:8000/7d4e06f8-d7b6-45f8-b59a-000945d5f382"/>
<skos:Concept rdf:about="http://localhost:8000/0c1ee567-9de6-44fb-8274-ffc487e017ef"/>
<skos:Concept rdf:about="http://localhost:8000/194c0230-49de-4c8b-96a8-882f13d3ce2f"/>
<skos:Concept rdf:about="http://localhost:8000/3d2b0c01-2271-44f0-9aae-21686468151b"/>
<skos:Concept rdf:about="http://localhost:8000/9e323767-98eb-40e0-a928-5c5ab5987d65"/>
<skos:Concept rdf:about="http://localhost:8000/fd370a17-49ed-4c5c-b609-cc1253ff1ecb"/>
<skos:Concept rdf:about="http://localhost:8000/07241e0f-ca32-4b81-b9e8-958e4caddc0f"/>
<skos:Concept rdf:about="http://localhost:8000/1387259a-4212-4125-837e-3d630c256acf"/>
<skos:Concept rdf:about="http://localhost:8000/1bd690ec-effb-4e7e-9aa7-371cfdf98ab3"/>
<skos:Concept rdf:about="http://localhost:8000/368e2783-b30d-409e-a968-628ab11fa382"/>
<skos:Concept rdf:about="http://localhost:8000/b439ad4f-8c25-46f2-b172-01fb8bfe7655"/>
<skos:Concept rdf:about="http://localhost:8000/fdc586c3-a44b-4142-ad56-c208fb4b4999"/>
<skos:Concept rdf:about="http://localhost:8000/1e5f43b8-16f2-493a-a9db-c05f07d33786"/>
<skos:Concept rdf:about="http://localhost:8000/4a432393-026a-42a9-972a-45077f8ab14b"/>
<skos:Concept rdf:about="http://localhost:8000/f5d7305e-49e8-4c01-8188-442a8f75fabb"/>
<skos:Concept rdf:about="http://localhost:8000/4de08727-2be7-4b4d-bdb8-f29f4a86fe61"/>
<skos:Concept rdf:about="http://localhost:8000/374168a7-fabc-44bd-89f2-95bed49a0372"/>
<skos:Concept rdf:about="http://localhost:8000/0c57e100-3bdc-46bf-bde5-f8e0032cb51f"/>
<skos:Concept rdf:about="http://localhost:8000/3d8263e9-3a7d-404e-a92b-25536cf60133"/>
<skos:Concept rdf:about="http://localhost:8000/30e18a63-67b5-4def-9ab0-5b3773ba22ff">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/6e9fc07b-392d-45dd-9b48-b8150684d09d"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/8a304889-9df5-4449-acbc-65115c362739"/>
</skos:member>
<skos:member rdf:resource="http://localhost:8000/87245fe4-812f-4dc2-8b9d-c1ea87867478"/>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/41128174-3382-4bfd-aa17-3d28a66330fc"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/41c7d770-f0ac-4233-8c3e-a7b681e93262"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/897ba379-82ac-4925-a3e6-9fbd2c931a53"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/a82f0f57-3178-40a1-a384-040e48deb3bd"/>
<skos:Concept rdf:about="http://localhost:8000/c3b1415f-36e9-4251-9fab-092b69e66047"/>
<skos:Concept rdf:about="http://localhost:8000/dc9539f3-71bb-4aee-b0d0-d2f22eea9d23"/>
<skos:Concept rdf:about="http://localhost:8000/022cd692-320f-4913-85d4-54d83abc7cb9">
<skos:member rdf:resource="http://localhost:8000/b245a11b-cf7e-4b1d-9d37-6ee86d859f3f"/>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/1aa30bed-1934-45f4-888e-1947e87f9973"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/79d7541f-7831-4c81-a8a1-ee600055bddd"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/f650f60a-99e6-45d0-b877-448afea192c1"/>
<skos:Concept rdf:about="http://localhost:8000/80506d62-00ee-44c7-870e-3ee8e2eee760">
<skos:member rdf:resource="http://localhost:8000/fdbaee06-b330-4ed8-9b7c-07c6aaf8f0bb"/>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/792850a2-c896-491d-b004-bfa4c5ac5e62"/>
<skos:Concept rdf:about="http://localhost:8000/0a5c88fe-9b31-4b94-b0e1-48663f819b79"/>
<skos:Concept rdf:about="http://localhost:8000/fef3c640-c464-44c0-a032-c3ddf9ee584f"/>
<skos:Concept rdf:about="http://localhost:8000/4475cecb-bf00-4c3f-b95d-90609a9ea7c5"/>
<skos:Concept rdf:about="http://localhost:8000/8d69b941-b662-4235-8671-289f5b444847"/>
<skos:Concept rdf:about="http://localhost:8000/7161ad7a-7ed4-43f5-b354-3287b3835da2"/>
<skos:Concept rdf:about="http://localhost:8000/2bc36055-ee70-4536-a076-ad77a09d9968"/>
<skos:Concept rdf:about="http://localhost:8000/90d53d57-7f49-455f-afa6-d8e59357dd48"/>
<skos:Concept rdf:about="http://localhost:8000/fec240f0-d862-4afa-8c80-ba4cbc3b077e"/>
<skos:Concept rdf:about="http://localhost:8000/7c2728d4-4665-47dd-aa26-b7f7fdeedfa5"/>
<skos:Concept rdf:about="http://localhost:8000/b6ca0113-61e5-40fa-aedd-840836d1ff79"/>
<skos:Concept rdf:about="http://localhost:8000/3f261f40-9d5d-45cc-a1ae-c732516230f0"/>
<skos:Concept rdf:about="http://localhost:8000/b47f60a6-8cc7-442e-8ed1-b0669c2b1092"/>
<skos:Concept rdf:about="http://localhost:8000/b7afe8e6-c7bb-480f-8dc4-52261d9810de"/>
<skos:Concept rdf:about="http://localhost:8000/46e56c73-cc44-409f-81f2-dd449ebf4def"/>
<skos:Concept rdf:about="http://localhost:8000/ffe4f51a-c04b-4f24-9b2a-45a135217635"/>
<skos:Concept rdf:about="http://localhost:8000/9035c4e3-693a-461e-b745-d9821aaa784c"/>
<skos:Concept rdf:about="http://localhost:8000/15380712-84b7-4294-b538-ce53d06c6e5e"/>
<skos:Concept rdf:about="http://localhost:8000/24d0f48f-e8c6-43cf-8468-e6cd7661090f"/>
<skos:Concept rdf:about="http://localhost:8000/f414e642-754b-44e4-bd58-7298eac88b9a"/>
<skos:Concept rdf:about="http://localhost:8000/3e42067d-8665-4754-ac1b-2c081d762aec"/>
<skos:Concept rdf:about="http://localhost:8000/20e2bcb8-f00c-4aec-a086-26af53e37b7d">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/21a3ed29-b9c5-4a66-9c06-f14dcdfbfab3"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/dd4bba28-0126-442c-aa09-2c53f2e5726c"/>
</skos:member>
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/89c67ad9-1ffb-44ac-9bcd-db4ce8df4cf8"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/4f898db1-c2ee-4360-8b6c-75eb0e5269d0"/>
<skos:Concept rdf:about="http://localhost:8000/a8dcc532-501d-406a-9097-ae20084c22e9"/>
<skos:Concept rdf:about="http://localhost:8000/cf2ab0f7-3bb6-4f91-8c61-a068ddd4a69b"/>
<skos:Concept rdf:about="http://localhost:8000/895cb294-6c69-4c6d-b393-5c696b845c66"/>
<skos:Concept rdf:about="http://localhost:8000/dc2337a4-b64b-423f-b845-965dae030ee5"/>
<skos:Concept rdf:about="http://localhost:8000/6af9ecff-8c4b-4fbc-9135-07eb5c24eb9a"/>
<skos:Concept rdf:about="http://localhost:8000/69490585-9d61-4039-9057-d147263fa14f"/>
<skos:Concept rdf:about="http://localhost:8000/66fc41a6-d074-4861-92f7-4e807da12916"/>
<skos:Concept rdf:about="http://localhost:8000/9ebf3275-bfd9-46a3-9fa0-ad83d1527b03"/>
<skos:Concept rdf:about="http://localhost:8000/965ece99-c369-4079-a9f6-d23e569057d3">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/b06ffcb4-e19b-46cc-b0c0-2a0c08d5ef47"/>
</skos:member>
<skos:member rdf:resource="http://localhost:8000/f650f60a-99e6-45d0-b877-448afea192c1"/>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/402c5ea6-5fb6-4595-8635-d92062a38a3f"/>
<skos:Concept rdf:about="http://localhost:8000/068a05c1-bd3e-4619-bb25-24b225321657"/>
<skos:Concept rdf:about="http://localhost:8000/cd3a80a1-2033-4c3d-a265-22166233174f"/>
<skos:Concept rdf:about="http://localhost:8000/94d39278-730d-49c2-a6ef-c395b99f4fc6"/>
<skos:Concept rdf:about="http://localhost:8000/3e7ecfd2-0f7b-468f-a30d-2fb5b618c4f2"/>
<skos:Concept rdf:about="http://localhost:8000/318846e4-3073-4e8f-9b1d-42d30a9eda03"/>
<skos:Concept rdf:about="http://localhost:8000/d0a29430-71fd-4bae-b738-1af410244484"/>
<skos:Concept rdf:about="http://localhost:8000/12694208-2acf-4926-abda-8dab0871825c"/>
<skos:Concept rdf:about="http://localhost:8000/3ca09c84-9ed5-4c12-8991-391d07e57395"/>
<skos:Concept rdf:about="http://localhost:8000/290fe7c1-60a4-4cfd-b374-bf378a75a767"/>
<skos:Concept rdf:about="http://localhost:8000/fbc90588-2a79-4cd3-8fa5-26ab452dd5a3"/>
<skos:Concept rdf:about="http://localhost:8000/e9cd8e41-4616-436a-a190-5c2a4cfd6eab"/>
<skos:Concept rdf:about="http://localhost:8000/cd5accbc-5c8a-40b6-a47b-bf28e791292c"/>
<skos:Concept rdf:about="http://localhost:8000/d4425ec3-4b81-48d0-9118-b43a9751ea8b"/>
<skos:Concept rdf:about="http://localhost:8000/ba6b5b79-47df-4441-8037-ce7d0b7d58fe"/>
<skos:Concept rdf:about="http://localhost:8000/3be2fe8a-6cfe-4c57-bb9d-ceed68670691"/>
<skos:Concept rdf:about="http://localhost:8000/c3ad28ce-a2d8-479a-b8f4-628e181f95ff"/>
<skos:Concept rdf:about="http://localhost:8000/0e6d3562-48fb-4c12-b639-acc86a3b7762"/>
<skos:Concept rdf:about="http://localhost:8000/bb9755fa-2da4-4beb-9447-acb45c2f7d5f"/>
<skos:Concept rdf:about="http://localhost:8000/82767a95-8d9d-4861-8278-d62d2da7c465"/>
<skos:Concept rdf:about="http://localhost:8000/d53ff5d8-8166-4e8a-a92f-fbcfaf5983d6"/>
<skos:Concept rdf:about="http://localhost:8000/24d9fec0-31f4-4740-bbce-7a4397719960"/>
<skos:Concept rdf:about="http://localhost:8000/a286f000-bcc0-45d2-9cea-41ddafb19e55"/>
<skos:Concept rdf:about="http://localhost:8000/d0e6f0c1-2233-4ebc-a089-7cd2a1fc3a42"/>
<skos:Concept rdf:about="http://localhost:8000/9b3712d8-a7ae-47d1-bbce-8a9c283b00cf"/>
<skos:Concept rdf:about="http://localhost:8000/e34f9e36-0afa-40a0-b525-d7c30ed9da0c"/>
<skos:Concept rdf:about="http://localhost:8000/dd231655-0a88-456a-bb9b-33b8cb58934d"/>
<skos:Concept rdf:about="http://localhost:8000/b26b8bf9-c8be-45fb-afe6-35bb649eecdf"/>
<skos:Concept rdf:about="http://localhost:8000/bf2cc9fa-8224-4035-a567-b9d9d6d96722"/>
<skos:Concept rdf:about="http://localhost:8000/2bd93e3a-1bcb-4e2b-b59c-6eacdd27ba6c"/>
<skos:Concept rdf:about="http://localhost:8000/daf23c0f-8c2d-4408-9cb2-697f528b6a87"/>
<skos:Concept rdf:about="http://localhost:8000/5ab46ba0-ae30-4f8e-ab64-0b124dbfcb49"/>
<skos:Concept rdf:about="http://localhost:8000/4158d4b9-69ba-44b5-8fd5-2295c9841633"/>
<skos:Concept rdf:about="http://localhost:8000/403103e2-126b-4a0e-bba7-d109e2e1a15c"/>
<skos:Concept rdf:about="http://localhost:8000/39f0df93-1cac-4a3a-9c7c-306c517b4f74"/>
<skos:Concept rdf:about="http://localhost:8000/5150ec5c-e816-4421-94da-ffd0ab62074d"/>
<skos:Concept rdf:about="http://localhost:8000/7a73602d-384f-4434-8794-50942ed40a6c"/>
<skos:Concept rdf:about="http://localhost:8000/e1419bea-183f-4d0f-997d-b3e394d851f4"/>
<skos:Concept rdf:about="http://localhost:8000/b9cabe77-846d-402d-adcd-bb43006c8c54"/>
<skos:Concept rdf:about="http://localhost:8000/d8dc6dad-0e63-444b-a0e3-0b82444b6349"/>
<skos:Concept rdf:about="http://localhost:8000/3d307152-ac44-463f-b8c2-bdbb82a7aae9"/>
<skos:Concept rdf:about="http://localhost:8000/61671c1d-b6b3-4af9-a329-cd5609eed336"/>
<skos:Concept rdf:about="http://localhost:8000/d2bf0a0d-921d-4e8d-b049-7f0d048f993f"/>
<skos:Concept rdf:about="http://localhost:8000/21921d6a-2294-4a62-8357-97cae58b61a6"/>
<skos:Concept rdf:about="http://localhost:8000/7d021a36-ae9e-40d0-bc9e-35484dec6394"/>
<skos:Concept rdf:about="http://localhost:8000/75d1d53c-284e-4ec1-9f46-e0743338b3eb"/>
<skos:Concept rdf:about="http://localhost:8000/7d2b2877-54ce-44a0-9f5a-b5acb5c79a4f"/>
<skos:Concept rdf:about="http://localhost:8000/70554156-baa3-4de8-9fff-85c2f54075cc"/>
<skos:Concept rdf:about="http://localhost:8000/bba2d102-5ace-4aef-bba0-3924cc4cac77"/>
<skos:Concept rdf:about="http://localhost:8000/2b24ad46-a388-47f6-bae1-1b1c41f80815"/>
<skos:Concept rdf:about="http://localhost:8000/f0cc8546-00dc-4ec5-805e-c1319268d161"/>
<skos:Concept rdf:about="http://localhost:8000/1c64bc4d-a403-4ff0-b579-ac5dbc880732"/>
<skos:Concept rdf:about="http://localhost:8000/88bed6b7-8dfd-4e9e-833e-d96bc6f92595"/>
<skos:Concept rdf:about="http://localhost:8000/6a3c8e77-0bbb-4010-aacc-3a3cafc22fd8"/>
<skos:Concept rdf:about="http://localhost:8000/4f289bc6-9867-433d-837e-7ffe4c024ad5"/>
<skos:Concept rdf:about="http://localhost:8000/157b95ca-ebc3-4613-986a-0d4d9d65b299"/>
<skos:Concept rdf:about="http://localhost:8000/d09226f1-79ca-4449-820a-b7d6032ab877"/>
<skos:Concept rdf:about="http://localhost:8000/7ac05ac7-657c-45ea-8079-f99171111b1d"/>
<skos:Concept rdf:about="http://localhost:8000/d3bbc701-d42f-400d-8825-16691e8ceb4e"/>
<skos:Concept rdf:about="http://localhost:8000/3dcae09a-14d5-419e-a050-144e78fbe306"/>
<skos:Concept rdf:about="http://localhost:8000/94eb0738-3fc6-490f-935e-d04f0340daf2"/>
<skos:Concept rdf:about="http://localhost:8000/60785b51-df13-403b-aa2d-f2df67192d13"/>
<skos:Concept rdf:about="http://localhost:8000/3d06f467-f354-4dbe-9efd-8df3f8cef701"/>
<skos:Concept rdf:about="http://localhost:8000/4a2185af-f080-44d8-8977-e14ef3257b9a">
<skos:member>
<skos:Concept rdf:about="http://localhost:8000/79d14415-db0c-4f54-94ee-7cd38ea1c0cd"/>
</skos:member>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/aa8f54f9-ba08-4243-b276-62a81805dda5"/>
<skos:Concept rdf:about="http://localhost:8000/037f5c10-3eb0-4325-b625-b8b6eabd4e5b"/>
<skos:Concept rdf:about="http://localhost:8000/9127a332-a135-42c2-ae0f-9206fe48b601"/>
<skos:Concept rdf:about="http://localhost:8000/1dba5d44-47a8-4441-a765-8a7ec318a857"/>
<skos:Concept rdf:about="http://localhost:8000/47a5426d-b0d4-4007-a695-74363f105850"/>
<skos:Concept rdf:about="http://localhost:8000/b7561b13-cc1d-4eb3-9d5a-b2f92e27c0cb"/>
<skos:Concept rdf:about="http://localhost:8000/89d64eac-4f8b-4012-8342-6bd538fae171"/>
<skos:Concept rdf:about="http://localhost:8000/2e6fc20d-e2c8-4b23-b323-c1bb748e1895"/>
<skos:Concept rdf:about="http://localhost:8000/b4a95ce0-253e-47d6-ba9e-3b9e42da83f6">
<skos:member rdf:resource="http://localhost:8000/5cfa5852-06ca-44b5-9969-2bb1157bec01"/>
<skos:member rdf:resource="http://localhost:8000/32d03b98-d4d5-46bb-9152-2b401a9e92bb"/>
<skos:member rdf:resource="http://localhost:8000/01b5458c-cb49-4da7-a7c8-a3213900fb30"/>
</skos:Concept>
<skos:Concept rdf:about="http://localhost:8000/74ea067c-5813-4f10-8aa9-c6f6bb1ec128"/>
<skos:Concept rdf:about="http://localhost:8000/11c57d99-eedf-4156-984a-aa82e197a568"/>
<skos:Concept rdf:about="http://localhost:8000/9e216c2d-b7ca-4496-9d56-ef3627659e72"/>
<skos:Concept rdf:about="http://localhost:8000/00f09747-091d-4358-90e3-750a259b756b"/>
<skos:Concept rdf:about="http://localhost:8000/46ceafac-c7f1-4dbb-b653-62569ceb3bbd"/>
<skos:Concept rdf:about="http://localhost:8000/72ddb6b0-c988-436a-881e-cfe0d452a5b0"/>
<skos:Concept rdf:about="http://localhost:8000/a69c5df6-7737-4f87-ad32-95ca8415c642"/>
<skos:Concept rdf:about="http://localhost:8000/e52e02e3-e182-4ddd-a5e9-8360971986ba"/>
<skos:Concept rdf:about="http://localhost:8000/3e60ffca-3232-4e4a-9870-ca55e2e19961"/>
<skos:Concept rdf:about="http://localhost:8000/fe0d72e8-59f7-4595-b7c0-7e99aa8563ab"/>
<skos:Concept rdf:about="http://localhost:8000/79034bb0-a41a-4470-8403-697c3c3d04b0"/>
<skos:Concept rdf:about="http://localhost:8000/166dada7-5318-4c5a-a9c8-7e545325be44"/>
<skos:Concept rdf:about="http://localhost:8000/0ca8da7e-f13a-45f8-aef6-4fa68ce4c0ef"/>
<skos:Concept rdf:about="http://localhost:8000/2f2c9d01-ff0d-45c3-9137-d9488f8cc078"/>
<skos:Concept rdf:about="http://localhost:8000/ae7a4977-9d1e-43f9-945a-591adef5cbdc"/>
<skos:Concept rdf:about="http://localhost:8000/076bfc03-3e35-4f82-9fbf-a480da55d2ad"/>
<skos:Concept rdf:about="http://localhost:8000/3115a3ed-f42d-48e1-a19d-df61879eec0d"/>
<skos:Concept rdf:about="http://localhost:8000/4f98dedc-8477-49f8-b080-0d00ac33b706"/>
<skos:Concept rdf:about="http://localhost:8000/94176d85-c71b-49a4-a84c-1b9c0ad2c50b"/>
<skos:Concept rdf:about="http://localhost:8000/4bf0d9a7-c43a-4fd2-94e0-a62c4e911994"/>
<skos:Concept rdf:about="http://localhost:8000/da1e990b-6e0e-4d2f-9e9c-6c26ab77b0bb"/>
<skos:Concept rdf:about="http://localhost:8000/b5009028-35ee-4c59-8516-f234a66eab2b"/>
<skos:Concept rdf:about="http://localhost:8000/7782f089-da7c-4f62-becd-7545615568f9"/>
<skos:Concept rdf:about="http://localhost:8000/532c5fec-bb23-4d94-86cd-aeef88f0f1c3"/>
<skos:Concept rdf:about="http://localhost:8000/6b4a2372-24bf-4900-b287-42bb4b212f61"/>
<skos:Concept rdf:about="http://localhost:8000/cbf5bedc-f2ef-4115-81e2-fb6426647d29"/>
<skos:Concept rdf:about="http://localhost:8000/8d37d262-855d-4103-9fc4-149d04387af2"/>
<skos:Concept rdf:about="http://localhost:8000/d7f8892b-a97f-49f4-9d25-9f7400333e68"/>
<skos:Concept rdf:about="http://localhost:8000/f5a181e7-db75-46f8-9a95-fafb596c7a08"/>
<skos:Concept rdf:about="http://localhost:8000/5b057049-3a53-46df-baff-f90cabb1d92f"/>
<skos:Concept rdf:about="http://localhost:8000/e4c0153f-bbca-41c2-9d5c-3f8902297d87"/>
<skos:Concept rdf:about="http://localhost:8000/593a22c2-963c-4b27-9ce0-93af2d9aa3ea"/>
<skos:Concept rdf:about="http://localhost:8000/3c7bb43e-9edf-4237-a0da-583cf7c40ebe"/>
<skos:Concept rdf:about="http://localhost:8000/cdf65893-e805-48ef-9113-81256fe00442"/>
<skos:Concept rdf:about="http://localhost:8000/8f4c70f1-3b60-4422-b66c-b93f7b9fa374"/>
<skos:Concept rdf:about="http://localhost:8000/82dde12e-90b7-4967-b8e6-d321785b330d"/>
<skos:Concept rdf:about="http://localhost:8000/f8e2e340-98d3-4bd8-9864-9070f4307553"/>
<skos:Concept rdf:about="http://localhost:8000/d0b0aa26-afca-4602-abda-bc26e3d47ba8"/>
<skos:Concept rdf:about="http://localhost:8000/b72132bb-0730-472f-a5b5-faa322f0c4c9"/>
<skos:Concept rdf:about="http://localhost:8000/743c6434-4d37-4933-b82a-f3f1b8d62c22"/>
<skos:Concept rdf:about="http://localhost:8000/a29d52be-ab11-440c-b247-51d5c28857ac"/>
<skos:Concept rdf:about="http://localhost:8000/c37f78f0-ac78-49e9-8873-d4a50a591425"/>
<skos:Concept rdf:about="http://localhost:8000/77c74570-2676-4d06-a439-7ef102259d40"/>
<skos:Concept rdf:about="http://localhost:8000/8ca05a2e-b409-46a7-841a-a78d485df7c8"/>
<skos:Concept rdf:about="http://localhost:8000/217c3bfe-5228-4077-983c-f32deb4482d1"/>
<skos:Concept rdf:about="http://localhost:8000/5f107b39-285b-4ddd-a32d-53fc8891c17d"/>
<skos:Concept rdf:about="http://localhost:8000/393a6aab-b744-4452-9530-653568c8d937"/>
<skos:Concept rdf:about="http://localhost:8000/9eb72802-ebe9-45f0-8fa0-32c05a1ec4f6"/>
<skos:Concept rdf:about="http://localhost:8000/6ff4dfd8-2e5b-4f26-9472-5a2422f7f04b"/>
<skos:Concept rdf:about="http://localhost:8000/134a70cd-7848-474e-96dd-422f896b6fcc"/>
<skos:Concept rdf:about="http://localhost:8000/52f75a1d-a1f3-4bdd-a54e-9ff71fd05c7b"/>
<skos:Concept rdf:about="http://localhost:8000/57903a1e-bfa6-43df-a79f-289363d8d52c"/>
<skos:Concept rdf:about="http://localhost:8000/f3941ff9-2629-486d-8c1b-763b3918c9b4"/>
<skos:Concept rdf:about="http://localhost:8000/b7fe59a0-57c4-4796-ae14-8d7f7cbf4163"/>
</rdf:RDF>"""

# Parse the XML data with namespaces
root = ET.fromstring(xml_data)

# Define a dictionary to store the extracted data
rdf_data = {}

# Process Collection elements
for collection in root.findall(
    ".//skos:Collection", namespaces={"skos": "http://www.w3.org/2004/02/skos/core#"}
):
    collection_data = {
        "@id": collection.get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
    }

    member_list = []

    for concept in collection.findall(
        ".//skos:member", namespaces={"skos": "http://www.w3.org/2004/02/skos/core#"}
    ):
        concept_data = {
            "@id": concept.find(
                ".//skos:Concept",
                namespaces={"skos": "http://www.w3.org/2004/02/skos/core#"},
            ).get("{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about")
        }
        member_list.append(concept_data)

    if member_list:
        collection_data["skos:member"] = member_list

    rdf_data[collection_data["@id"]] = collection_data

# Output the extracted data as JSON
output_json = json.dumps(rdf_data, indent=2)
print(output_json)