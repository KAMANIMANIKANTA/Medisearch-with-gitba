from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["medisearch"]
medicines_collection = db["medicines"]

# List of medicines to insert
medicines_data = [
    {
        "name": "paracetamol",
        "description": {
            "usage": {
                "short": "Used to treat pain and inflammation.",
                "detailed": "Paracetamol is commonly used to relieve mild to moderate pain such as headaches, toothaches, muscle pain, and menstrual cramps."
            },
            "why_to_use": {
                "short": "Effective for reducing fever and relieving pain.",
                "detailed": "Paracetamol is an analgesic and antipyretic agent, making it effective in reducing fever by acting on the hypothalamic heat-regulating center."
            },
            "advantages": {
                "short": "Fast-acting, over-the-counter availability.",
                "detailed": "One of the major advantages of paracetamol is its fast action in pain relief, usually within 30 minutes of administration."
            },
            "disadvantages": {
                "short": "Can cause stomach upset if taken on an empty stomach.",
                "detailed": "Although generally safe, taking paracetamol on an empty stomach may lead to mild gastric discomfort."
            },
            "side_effects": {
                "short": "Nausea, dizziness, allergic reactions.",
                "detailed": "Common side effects of paracetamol include nausea and dizziness. Rarely, it can cause allergic reactions such as rash, itching."
            }
        }
    },
    {
        "name": "cetirizine",
        "description": {
            "usage": {
                "short": "Used to treat allergies.",
                "detailed": "Cetirizine is an antihistamine used to relieve allergy symptoms such as watery eyes, runny nose, itching eyes/nose, and sneezing."
            },
            "why_to_use": {
                "short": "Effective in reducing allergic reactions.",
                "detailed": "Cetirizine blocks the effects of histamine, a substance in the body that causes allergic symptoms."
            },
            "advantages": {
                "short": "Non-drowsy, long-lasting effect.",
                "detailed": "Cetirizine is popular due to its non-drowsy formula and long-lasting effect, providing relief for up to 24 hours."
            },
            "disadvantages": {
                "short": "May cause dry mouth.",
                "detailed": "Cetirizine can occasionally cause dryness of the mouth, nose, and throat, especially when used for prolonged periods."
            },
            "side_effects": {
                "short": "Drowsiness, dry mouth.",
                "detailed": "Common side effects include mild drowsiness, dry mouth, and, in some cases, fatigue."
            }
        }
    },
    {
        "name": "saridon",
        "description": {
            "usage": {
                "short": "Used to treat headaches and migraines.",
                "detailed": "Saridon is a combination pain relief medicine used to treat headaches, toothaches, and muscular pain."
            },
            "why_to_use": {
                "short": "Fast pain relief.",
                "detailed": "Saridon is effective because it combines paracetamol, propyphenazone, and caffeine to quickly relieve pain and enhance alertness."
            },
            "advantages": {
                "short": "Quick action, combination therapy.",
                "detailed": "Saridon's combination formula allows for faster relief compared to single-ingredient analgesics."
            },
            "disadvantages": {
                "short": "Not suitable for children under 12.",
                "detailed": "Saridon is not recommended for children under 12 due to the risk of side effects related to propyphenazone."
            },
            "side_effects": {
                "short": "Stomach upset, allergic reactions.",
                "detailed": "Possible side effects include stomach discomfort and, in rare cases, allergic reactions like skin rashes."
            }
        }
    },
    {
        "name": "ibuprofen",
        "description": {
            "usage": {
                "short": "Used to reduce pain, fever, and inflammation.",
                "detailed": "Ibuprofen is an NSAID (non-steroidal anti-inflammatory drug) used to treat mild to moderate pain, inflammation, and fever."
            },
            "why_to_use": {
                "short": "Effective for reducing inflammation.",
                "detailed": "Ibuprofen works by reducing hormones that cause inflammation and pain in the body."
            },
            "advantages": {
                "short": "Effective for a wide range of pain types.",
                "detailed": "Ibuprofen is widely available and effective for various pain types including arthritis, menstrual cramps, and headaches."
            },
            "disadvantages": {
                "short": "May cause stomach ulcers if overused.",
                "detailed": "Prolonged use of ibuprofen can cause stomach ulcers and gastrointestinal bleeding, especially in high doses."
            },
            "side_effects": {
                "short": "Stomach pain, nausea, heartburn.",
                "detailed": "Common side effects include stomach pain, nausea, and heartburn; rare cases may involve liver or kidney issues."
            }
        }
    },
    {
        "name": "aspirin",
        "description": {
            "usage": {
                "short": "Used to reduce pain and fever.",
                "detailed": "Aspirin is used for pain relief, fever reduction, and anti-inflammatory purposes, commonly for headaches and minor aches."
            },
            "why_to_use": {
                "short": "Reduces inflammation and prevents blood clots.",
                "detailed": "Aspirin is also used to prevent blood clots, reducing the risk of heart attacks and strokes."
            },
            "advantages": {
                "short": "Anti-inflammatory and blood-thinning properties.",
                "detailed": "Aspirin’s unique combination of anti-inflammatory and anticoagulant effects make it valuable for heart patients."
            },
            "disadvantages": {
                "short": "Risk of stomach bleeding.",
                "detailed": "Aspirin can cause stomach irritation and bleeding, particularly in those with a history of ulcers or bleeding disorders."
            },
            "side_effects": {
                "short": "Stomach upset, bleeding risk.",
                "detailed": "Potential side effects include stomach upset, ringing in the ears, and a higher risk of bleeding."
            }
        }
    },
    # Add remaining entries here up to "hydrochlorothiazide"...
    {
        "name": "hydrochlorothiazide",
        "description": {
            "usage": {
                "short": "Used to treat high blood pressure and fluid retention.",
                "detailed": "Hydrochlorothiazide is a thiazide diuretic that helps your body get rid of extra salt and water through urine."
            },
            "why_to_use": {
                "short": "Helps manage blood pressure and swelling.",
                "detailed": "It is effective in lowering blood pressure and reducing swelling caused by various conditions, including heart failure."
            },
            "advantages": {
                "short": "Widely used, effective.",
                "detailed": "Hydrochlorothiazide is one of the most commonly prescribed diuretics due to its effectiveness and safety profile."
            },
            "disadvantages": {
                "short": "Can cause electrolyte imbalances.",
                "detailed": "Potential side effects include low potassium levels and other electrolyte disturbances, which may require monitoring."
            },
            "side_effects": {
                "short": "Dizziness, frequent urination.",
                "detailed": "Common side effects include dizziness and an increased need to urinate, particularly when starting the medication."
            }
        }
    },  # <-- Corrected missing comma here
    {
        "name": "levothyroxine",
        "description": {
            "usage": {
                "short": "Used to treat hypothyroidism.",
                "detailed": "Levothyroxine is a synthetic thyroid hormone used to treat an underactive thyroid (hypothyroidism)."
            },
            "why_to_use": {
                "short": "Replaces thyroid hormone.",
                "detailed": "Levothyroxine restores the proper hormone levels in the body, helping to maintain normal metabolism."
            },
            "advantages": {
                "short": "Well tolerated, effective.",
                "detailed": "It is the most commonly prescribed medication for hypothyroidism, and is effective in maintaining thyroid function."
            },
            "disadvantages": {
                "short": "Requires regular blood tests.",
                "detailed": "Patients need regular blood tests to monitor thyroid hormone levels and adjust dosage."
            },
            "side_effects": {
                "short": "Fatigue, weight changes.",
                "detailed": "Side effects may include weight changes, fatigue, and in rare cases, heart palpitations."
            }
        }
    },  # <-- Added missing comma here
    {
        "name": "rosuvastatin",
        "description": {
            "usage": {
                "short": "Used to lower cholesterol.",
                "detailed": "Rosuvastatin is a statin that lowers levels of 'bad' cholesterol (LDL) and triglycerides in the blood."
            },
            "why_to_use": {
                "short": "Reduces the risk of heart disease.",
                "detailed": "By lowering cholesterol, rosuvastatin reduces the risk of heart attack, stroke, and other heart conditions."
            },
            "advantages": {
                "short": "Effective in lowering cholesterol.",
                "detailed": "It is particularly effective in reducing cholesterol levels, especially in patients at high risk of cardiovascular disease."
            },
            "disadvantages": {
                "short": "May cause muscle pain.",
                "detailed": "Some users may experience muscle pain or weakness, which can vary in severity."
            },
            "side_effects": {
                "short": "Muscle pain, liver enzyme abnormalities.",
                "detailed": "Possible side effects include muscle pain and changes in liver enzymes."
            }
        }
    },
    {
    "name": "clonazepam",
    "description": {
        "usage": {
            "short": "Used to treat anxiety and seizures.",
            "detailed": "Clonazepam is a benzodiazepine used to control seizures and relieve anxiety or panic attacks."
        },
        "why_to_use": {
            "short": "Effective for seizure control and anxiety relief.",
            "detailed": "Clonazepam works by calming the brain and nerves, making it effective for anxiety disorders and seizures."
        },
        "advantages": {
            "short": "Works quickly to relieve anxiety.",
            "detailed": "It is often prescribed for short-term use due to its fast action in relieving anxiety and preventing seizures."
        },
        "disadvantages": {
            "short": "Can be habit-forming.",
            "detailed": "Long-term use can lead to dependence or tolerance, so it is usually prescribed for short-term use."
        },
        "side_effects": {
            "short": "Drowsiness, dizziness.",
            "detailed": "Common side effects include drowsiness, dizziness, and coordination problems."
        }
    }
},
{
    "name": "pregabalin",
    "description": {
        "usage": {
            "short": "Used to treat nerve pain and seizures.",
            "detailed": "Pregabalin is used to relieve nerve pain caused by conditions such as fibromyalgia and can also treat seizures."
        },
        "why_to_use": {
            "short": "Helps control nerve pain effectively.",
            "detailed": "Pregabalin alters the way the body senses pain, making it effective for nerve pain."
        },
        "advantages": {
            "short": "Effective for chronic pain.",
            "detailed": "Pregabalin is particularly useful for managing chronic pain conditions, including diabetic nerve pain."
        },
        "disadvantages": {
            "short": "May cause drowsiness.",
            "detailed": "Common side effects include drowsiness, dizziness, and weight gain."
        },
        "side_effects": {
            "short": "Drowsiness, dizziness.",
            "detailed": "Possible side effects include drowsiness, dizziness, and blurred vision."
        }
    }
},
{
    "name": "duloxetine",
    "description": {
        "usage": {
            "short": "Used to treat depression and nerve pain.",
            "detailed": "Duloxetine is an antidepressant that is also used to relieve nerve pain in conditions like diabetes or fibromyalgia."
        },
        "why_to_use": {
            "short": "Relieves depression and pain.",
            "detailed": "Duloxetine affects chemicals in the brain that may be unbalanced in people with depression, anxiety, or chronic pain."
        },
        "advantages": {
            "short": "Treats both pain and mood disorders.",
            "detailed": "It is effective for treating both depression and the physical symptoms of pain, offering dual benefits."
        },
        "disadvantages": {
            "short": "May take several weeks to take effect.",
            "detailed": "It may take a few weeks before duloxetine starts to relieve symptoms of depression and pain."
        },
        "side_effects": {
            "short": "Nausea, dizziness.",
            "detailed": "Common side effects include nausea, dry mouth, and dizziness."
        }
    }
},
{
    "name": "carvedilol",
    "description": {
        "usage": {
            "short": "Used to treat high blood pressure and heart failure.",
            "detailed": "Carvedilol is a beta-blocker used to lower blood pressure and improve heart function in people with heart failure."
        },
        "why_to_use": {
            "short": "Improves heart function and reduces blood pressure.",
            "detailed": "Carvedilol helps the heart pump more efficiently, lowering blood pressure and reducing the risk of heart failure complications."
        },
        "advantages": {
            "short": "Protects the heart in people with heart failure.",
            "detailed": "It helps protect the heart from further damage, reducing the risk of hospitalization and death."
        },
        "disadvantages": {
            "short": "May cause dizziness and fatigue.",
            "detailed": "Common side effects include feeling tired and dizzy, especially when starting the medication."
        },
        "side_effects": {
            "short": "Dizziness, fatigue.",
            "detailed": "Common side effects include dizziness, fatigue, and weight gain."
        }
    }
},
{
    "name": "fluoxetine",
    "description": {
        "usage": {
            "short": "Used to treat depression and anxiety.",
            "detailed": "Fluoxetine is a selective serotonin reuptake inhibitor (SSRI) used to treat depression, anxiety, and panic attacks."
        },
        "why_to_use": {
            "short": "Helps improve mood and reduce anxiety.",
            "detailed": "Fluoxetine increases serotonin levels in the brain, which helps improve mood and reduce anxiety."
        },
        "advantages": {
            "short": "Effective for depression and anxiety.",
            "detailed": "Fluoxetine is widely prescribed due to its effectiveness in treating depression and anxiety disorders."
        },
        "disadvantages": {
            "short": "May cause insomnia and restlessness.",
            "detailed": "Some users may experience insomnia or restlessness, especially when starting the medication."
        },
        "side_effects": {
            "short": "Nausea, insomnia.",
            "detailed": "Common side effects include nausea, insomnia, and dry mouth."
        }
    }
},
{
    "name": "pantoprazole",
    "description": {
        "usage": {
            "short": "Used to treat acid reflux and GERD.",
            "detailed": "Pantoprazole is a proton pump inhibitor (PPI) that reduces stomach acid, relieving symptoms of acid reflux and preventing ulcers."
        },
        "why_to_use": {
            "short": "Reduces stomach acid effectively.",
            "detailed": "Pantoprazole reduces the amount of acid produced in the stomach, providing relief from heartburn and preventing ulcers."
        },
        "advantages": {
            "short": "Long-lasting relief from acid reflux.",
            "detailed": "It provides relief from acid reflux symptoms for up to 24 hours with a single daily dose."
        },
        "disadvantages": {
            "short": "May take a few days to take full effect.",
            "detailed": "Pantoprazole does not provide immediate relief and may take a few days to start working."
        },
        "side_effects": {
            "short": "Headache, nausea.",
            "detailed": "Side effects may include headache, nausea, and, in rare cases, low magnesium levels."
        }
    }
},
{
    "name": "spironolactone",
    "description": {
        "usage": {
            "short": "Used to treat fluid retention and high blood pressure.",
            "detailed": "Spironolactone is a diuretic that helps the body eliminate excess water and salt, used to treat conditions like heart failure and high blood pressure."
        },
        "why_to_use": {
            "short": "Helps reduce swelling and blood pressure.",
            "detailed": "Spironolactone works by blocking aldosterone, a hormone that causes the body to retain water, thereby reducing blood pressure and swelling."
        },
        "advantages": {
            "short": "Effective for fluid retention and hormone-related conditions.",
            "detailed": "In addition to treating heart failure, spironolactone is effective for conditions like polycystic ovary syndrome (PCOS)."
        },
        "disadvantages": {
            "short": "May cause high potassium levels.",
            "detailed": "Spironolactone can raise potassium levels, so regular monitoring is necessary."
        },
        "side_effects": {
            "short": "Increased potassium, breast tenderness.",
            "detailed": "Common side effects include increased potassium levels and breast tenderness or enlargement."
        }
    }
},
{
    "name": "alprazolam",
    "description": {
        "usage": {
            "short": "Used to treat anxiety and panic disorders.",
            "detailed": "Alprazolam is a benzodiazepine used to treat anxiety disorders, panic attacks, and anxiety caused by depression."
        },
        "why_to_use": {
            "short": "Provides fast relief from anxiety symptoms.",
            "detailed": "Alprazolam works by enhancing the effects of GABA, a neurotransmitter that promotes calmness and reduces anxiety."
        },
        "advantages": {
            "short": "Fast-acting relief from anxiety.",
            "detailed": "It works quickly to relieve symptoms, making it effective for acute anxiety attacks."
        },
        "disadvantages": {
            "short": "Can cause dependence and withdrawal.",
            "detailed": "Alprazolam has a high potential for abuse and dependence, and discontinuation can lead to withdrawal symptoms."
        },
        "side_effects": {
            "short": "Drowsiness, dizziness.",
            "detailed": "Common side effects include drowsiness, dizziness, and coordination problems."
        }
    }
},
{
    "name": "valacyclovir",
    "description": {
        "usage": {
            "short": "Used to treat viral infections.",
            "detailed": "Valacyclovir is an antiviral medication used to treat infections such as herpes simplex, shingles, and cold sores."
        },
        "why_to_use": {
            "short": "Reduces the severity of viral outbreaks.",
            "detailed": "Valacyclovir helps stop the growth of the virus, reducing the severity and frequency of outbreaks."
        },
        "advantages": {
            "short": "Effective for managing viral infections.",
            "detailed": "It is commonly prescribed for both initial and recurrent outbreaks of herpes and shingles."
        },
        "disadvantages": {
            "short": "Requires early treatment to be effective.",
            "detailed": "For the best results, valacyclovir must be taken at the first sign of an outbreak."
        },
        "side_effects": {
            "short": "Headache, nausea.",
            "detailed": "Common side effects include headache, nausea, and occasionally, abdominal pain."
        }
    }
},
{
    "name": "allopurinol",
    "description": {
        "usage": {
            "short": "Used to treat gout and kidney stones.",
            "detailed": "Allopurinol reduces uric acid production in the body, preventing gout attacks and kidney stones."
        },
        "why_to_use": {
            "short": "Reduces uric acid levels effectively.",
            "detailed": "It helps prevent the formation of uric acid crystals in the joints and kidneys."
        },
        "advantages": {
            "short": "Effective long-term treatment for gout.",
            "detailed": "Allopurinol is widely used to prevent gout attacks and treat chronic cases."
        },
        "disadvantages": {
            "short": "May cause initial worsening of gout symptoms.",
            "detailed": "Some patients may experience an increase in gout attacks when starting treatment."
        },
        "side_effects": {
            "short": "Rash, nausea.",
            "detailed": "Common side effects include rash, nausea, and in rare cases, liver enzyme abnormalities."
        }
    }
},
{
    "name": "sitagliptin",
    "description": {
        "usage": {
            "short": "Used to manage type 2 diabetes.",
            "detailed": "Sitagliptin is an oral diabetes medication that helps control blood sugar by regulating insulin levels."
        },
        "why_to_use": {
            "short": "Helps lower blood sugar levels.",
            "detailed": "Sitagliptin works by increasing the levels of incretin hormones, which help control blood sugar levels after meals."
        },
        "advantages": {
            "short": "Helps manage blood sugar without causing hypoglycemia.",
            "detailed": "It effectively controls blood sugar with a low risk of causing low blood sugar (hypoglycemia)."
        },
        "disadvantages": {
            "short": "May cause joint pain in some patients.",
            "detailed": "In rare cases, sitagliptin has been associated with severe joint pain."
        },
        "side_effects": {
            "short": "Headache, sore throat.",
            "detailed": "Common side effects include headache, sore throat, and upper respiratory tract infections."
        }
    }
},
{
    "name": "pravastatin",
    "description": {
        "usage": {
            "short": "Used to lower cholesterol.",
            "detailed": "Pravastatin is a statin that helps lower levels of bad cholesterol (LDL) and raise levels of good cholesterol (HDL)."
        },
        "why_to_use": {
            "short": "Reduces the risk of heart attack and stroke.",
            "detailed": "By lowering cholesterol levels, pravastatin reduces the risk of cardiovascular events such as heart attack and stroke."
        },
        "advantages": {
            "short": "Well-tolerated cholesterol-lowering medication.",
            "detailed": "Pravastatin is generally well tolerated and effective in managing cholesterol levels."
        },
        "disadvantages": {
            "short": "May cause muscle pain in some users.",
            "detailed": "Some patients report muscle pain or weakness, a known side effect of statins."
        },
        "side_effects": {
            "short": "Muscle pain, nausea.",
            "detailed": "Common side effects include mild muscle pain, nausea, and digestive issues."
        }
    }
},
{
    "name": "morphine",
    "description": {
        "usage": {
            "short": "Used to treat severe pain.",
            "detailed": "Morphine is an opioid pain medication used to relieve moderate to severe pain, particularly after surgery or injury."
        },
        "why_to_use": {
            "short": "Effective for severe pain relief.",
            "detailed": "Morphine works by blocking pain signals to the brain, providing relief for severe pain."
        },
        "advantages": {
            "short": "Very effective for severe pain.",
            "detailed": "It is one of the most potent painkillers available, making it essential for pain management in critical situations."
        },
        "disadvantages": {
            "short": "High risk of dependence and overdose.",
            "detailed": "Due to its potency, morphine carries a high risk of abuse, dependence, and overdose."
        },
        "side_effects": {
            "short": "Drowsiness, constipation.",
            "detailed": "Common side effects include drowsiness, constipation, and nausea."
        }
    }
},
{
    "name": "tramadol",
    "description": {
        "usage": {
            "short": "Used to treat moderate to severe pain.",
            "detailed": "Tramadol is an opioid analgesic used for the treatment of moderate to severe pain."
        },
        "why_to_use": {
            "short": "Effective for short-term pain management.",
            "detailed": "Tramadol works by altering how the brain senses pain, making it effective for short-term pain relief."
        },
        "advantages": {
            "short": "Less addictive than stronger opioids.",
            "detailed": "Compared to stronger opioids like morphine, tramadol is less likely to cause dependence."
        },
        "disadvantages": {
            "short": "Risk of addiction and overdose.",
            "detailed": "Although less addictive than stronger opioids, tramadol still carries a risk of addiction and overdose."
        },
        "side_effects": {
            "short": "Nausea, dizziness.",
            "detailed": "Common side effects include nausea, dizziness, and drowsiness."
        }
    }
},
{
    "name": "simvastatin",
    "description": {
        "usage": {
            "short": "Used to lower cholesterol.",
            "detailed": "Simvastatin is a statin medication that lowers levels of 'bad' cholesterol (LDL) and triglycerides in the blood."
        },
        "why_to_use": {
            "short": "Reduces the risk of heart disease.",
            "detailed": "Simvastatin helps lower cholesterol levels, reducing the risk of heart disease and stroke."
        },
        "advantages": {
            "short": "Highly effective for lowering cholesterol.",
            "detailed": "It is one of the most prescribed statins due to its effectiveness in reducing LDL cholesterol levels."
        },
        "disadvantages": {
            "short": "May cause muscle pain or weakness.",
            "detailed": "Some patients experience muscle pain or weakness, which can range from mild to severe."
        },
        "side_effects": {
            "short": "Muscle pain, digestive issues.",
            "detailed": "Common side effects include muscle pain, nausea, and liver enzyme abnormalities."
        }
    }
},
{
    "name": "celecoxib",
    "description": {
        "usage": {
            "short": "Used to reduce pain and inflammation.",
            "detailed": "Celecoxib is a COX-2 inhibitor NSAID used to treat arthritis, menstrual pain, and other inflammatory conditions."
        },
        "why_to_use": {
            "short": "Effective for arthritis pain.",
            "detailed": "Celecoxib is particularly effective in treating arthritis pain by reducing inflammation and joint discomfort."
        },
        "advantages": {
            "short": "Less risk of stomach problems than other NSAIDs.",
            "detailed": "Celecoxib has a lower risk of causing stomach ulcers and bleeding compared to other NSAIDs."
        },
        "disadvantages": {
            "short": "May increase the risk of heart attack or stroke.",
            "detailed": "Long-term use of celecoxib, especially at high doses, may increase the risk of cardiovascular problems."
        },
        "side_effects": {
            "short": "Stomach upset, dizziness.",
            "detailed": "Side effects may include stomach upset, dizziness, and in rare cases, cardiovascular issues."
        }
    }
},
{
    "name": "loratadine",
    "description": {
        "usage": {
            "short": "Used to treat allergies.",
            "detailed": "Loratadine is an antihistamine used to relieve allergy symptoms such as runny nose, itchy eyes, and sneezing."
        },
        "why_to_use": {
            "short": "Non-drowsy formula for allergy relief.",
            "detailed": "Loratadine is popular due to its non-drowsy formulation and effectiveness in providing relief from allergic reactions."
        },
        "advantages": {
            "short": "Long-lasting effect without sedation.",
            "detailed": "Loratadine offers up to 24 hours of relief from allergy symptoms without causing significant drowsiness."
        },
        "disadvantages": {
            "short": "May cause dry mouth or fatigue.",
            "detailed": "Common side effects include dry mouth, headache, and mild fatigue."
        },
        "side_effects": {
            "short": "Dry mouth, headache.",
            "detailed": "Side effects may include dry mouth, headache, and occasional dizziness."
        }
    }
},
{
    "name": "baclofen",
    "description": {
        "usage": {
            "short": "Used to treat muscle spasms.",
            "detailed": "Baclofen is a muscle relaxant used to relieve muscle spasms caused by conditions such as multiple sclerosis or spinal cord injuries."
        },
        "why_to_use": {
            "short": "Helps relieve muscle tightness and spasms.",
            "detailed": "Baclofen helps by relaxing the muscles, relieving stiffness and discomfort caused by spasms."
        },
        "advantages": {
            "short": "Effective for muscle spasticity.",
            "detailed": "It is commonly used to treat muscle spasticity in patients with multiple sclerosis or spinal injuries."
        },
        "disadvantages": {
            "short": "May cause drowsiness and dizziness.",
            "detailed": "Common side effects include drowsiness, dizziness, and occasionally weakness."
        },
        "side_effects": {
            "short": "Drowsiness, weakness.",
            "detailed": "Common side effects include drowsiness, dizziness, and muscle weakness."
        }
    }
},
{
    "name": "montelukast",
    "description": {
        "usage": {
            "short": "Used to prevent asthma and allergy symptoms.",
            "detailed": "Montelukast is a leukotriene receptor antagonist used to prevent asthma attacks and relieve symptoms of allergies."
        },
        "why_to_use": {
            "short": "Helps control asthma and allergy symptoms.",
            "detailed": "Montelukast blocks leukotrienes, chemicals in the body that cause asthma symptoms and allergic reactions."
        },
        "advantages": {
            "short": "Effective for long-term asthma management.",
            "detailed": "It helps prevent wheezing, difficulty breathing, and other asthma symptoms."
        },
        "disadvantages": {
            "short": "May cause mood changes in some patients.",
            "detailed": "In rare cases, montelukast has been associated with mood changes such as depression or agitation."
        },
        "side_effects": {
            "short": "Headache, stomach pain.",
            "detailed": "Common side effects include headache, stomach pain, and sometimes insomnia."
        }
    }
},
{
    "name": "tamsulosin",
    "description": {
        "usage": {
            "short": "Used to treat symptoms of an enlarged prostate (BPH).",
            "detailed": "Tamsulosin is an alpha-blocker that relaxes the muscles in the prostate and bladder neck, making it easier to urinate."
        },
        "why_to_use": {
            "short": "Helps improve urine flow.",
            "detailed": "Tamsulosin helps relieve the symptoms of benign prostatic hyperplasia (BPH) by improving the flow of urine."
        },
        "advantages": {
            "short": "Effective for BPH without lowering blood pressure.",
            "detailed": "Tamsulosin selectively targets the prostate muscles without significantly affecting blood pressure."
        },
        "disadvantages": {
            "short": "May cause dizziness or retrograde ejaculation.",
            "detailed": "Common side effects include dizziness and retrograde ejaculation (where semen enters the bladder instead of exiting through the penis)."
        },
        "side_effects": {
            "short": "Dizziness, retrograde ejaculation.",
            "detailed": "Common side effects include dizziness, headache, and fatigue."
        }
    }
},
{
    "name": "zolpidem",
    "description": {
        "usage": {
            "short": "Used to treat insomnia.",
            "detailed": "Zolpidem is a sedative-hypnotic used to help people fall asleep and stay asleep."
        },
        "why_to_use": {
            "short": "Helps with sleep initiation.",
            "detailed": "Zolpidem is effective in treating sleep onset issues and improving overall sleep quality."
        },
        "advantages": {
            "short": "Works quickly to induce sleep.",
            "detailed": "Zolpidem starts working within 30 minutes, making it a quick solution for those who struggle to fall asleep."
        },
        "disadvantages": {
            "short": "May cause dependency.",
            "detailed": "Long-term use of zolpidem may lead to dependency and withdrawal symptoms."
        },
        "side_effects": {
            "short": "Drowsiness, dizziness.",
            "detailed": "Common side effects include drowsiness, dizziness, and sometimes memory issues."
        }
    }
},
{
    "name": "clindamycin",
    "description": {
        "usage": {
            "short": "Used to treat bacterial infections.",
            "detailed": "Clindamycin is an antibiotic effective in treating infections caused by anaerobic bacteria and some protozoal diseases."
        },
        "why_to_use": {
            "short": "Effective against bacterial infections.",
            "detailed": "Clindamycin works by stopping the growth of bacteria, making it effective against various bacterial infections."
        },
        "advantages": {
            "short": "Effective in treating skin and soft tissue infections.",
            "detailed": "Commonly used to treat infections in the skin, bones, joints, and abdomen."
        },
        "disadvantages": {
            "short": "May cause gastrointestinal upset.",
            "detailed": "Clindamycin is known to cause gastrointestinal disturbances, including diarrhea and, in some cases, colitis."
        },
        "side_effects": {
            "short": "Diarrhea, nausea.",
            "detailed": "Common side effects include nausea, diarrhea, and stomach discomfort."
        }
    }
},
{
    "name": "doxycycline",
    "description": {
        "usage": {
            "short": "Used to treat bacterial infections and acne.",
            "detailed": "Doxycycline is a tetracycline antibiotic that treats a variety of bacterial infections, including respiratory infections, acne, and certain sexually transmitted infections."
        },
        "why_to_use": {
            "short": "Effective in treating a wide range of infections.",
            "detailed": "Doxycycline inhibits the growth of bacteria, treating conditions like acne, urinary tract infections, and respiratory infections."
        },
        "advantages": {
            "short": "Effective against acne and bacterial infections.",
            "detailed": "Doxycycline is often prescribed for acne treatment due to its effectiveness in reducing bacterial growth and inflammation."
        },
        "disadvantages": {
            "short": "May cause sun sensitivity.",
            "detailed": "Patients using doxycycline may experience increased sensitivity to sunlight, leading to easier sunburns."
        },
        "side_effects": {
            "short": "Nausea, sun sensitivity.",
            "detailed": "Common side effects include nausea, upset stomach, and sensitivity to sunlight."
        }
    }
},
{
    "name": "mirtazapine",
    "description": {
        "usage": {
            "short": "Used to treat depression.",
            "detailed": "Mirtazapine is an antidepressant that helps to restore the balance of neurotransmitters in the brain, improving mood."
        },
        "why_to_use": {
            "short": "Effective for improving mood and appetite.",
            "detailed": "Mirtazapine is known to help alleviate symptoms of depression while improving appetite and sleep."
        },
        "advantages": {
            "short": "Improves sleep and reduces anxiety.",
            "detailed": "It is effective in treating depression with associated anxiety and sleep disturbances."
        },
        "disadvantages": {
            "short": "May cause weight gain.",
            "detailed": "Mirtazapine is known to increase appetite, which can lead to weight gain in some patients."
        },
        "side_effects": {
            "short": "Drowsiness, weight gain.",
            "detailed": "Common side effects include drowsiness, increased appetite, and weight gain."
        }
    }
},
{
    "name": "rivaroxaban",
    "description": {
        "usage": {
            "short": "Used to prevent blood clots.",
            "detailed": "Rivaroxaban is an anticoagulant that helps prevent and treat blood clots in conditions like deep vein thrombosis (DVT) and pulmonary embolism (PE)."
        },
        "why_to_use": {
            "short": "Prevents stroke and blood clots.",
            "detailed": "Rivaroxaban is prescribed to prevent stroke and systemic embolism in patients with atrial fibrillation."
        },
        "advantages": {
            "short": "Does not require frequent blood monitoring.",
            "detailed": "Unlike some other anticoagulants, rivaroxaban does not require frequent blood tests to monitor its effectiveness."
        },
        "disadvantages": {
            "short": "Risk of bleeding.",
            "detailed": "As with all anticoagulants, there is an increased risk of bleeding, including internal bleeding."
        },
        "side_effects": {
            "short": "Bleeding, dizziness.",
            "detailed": "Side effects include an increased risk of bleeding and occasional dizziness."
        }
    }
},
{
    "name": "lamotrigine",
    "description": {
        "usage": {
            "short": "Used to treat seizures and bipolar disorder.",
            "detailed": "Lamotrigine is an anticonvulsant medication used to treat seizures in patients with epilepsy and mood episodes in bipolar disorder."
        },
        "why_to_use": {
            "short": "Controls seizures and stabilizes mood.",
            "detailed": "Lamotrigine is effective in managing seizure disorders and preventing mood episodes in bipolar patients."
        },
        "advantages": {
            "short": "Effective for long-term mood stabilization.",
            "detailed": "It is widely used in the long-term management of bipolar disorder to prevent depressive and manic episodes."
        },
        "disadvantages": {
            "short": "May cause skin rashes.",
            "detailed": "Lamotrigine is known to cause skin rashes, and in rare cases, severe life-threatening conditions like Stevens-Johnson syndrome."
        },
        "side_effects": {
            "short": "Rash, dizziness.",
            "detailed": "Common side effects include dizziness, blurred vision, and skin rashes."
        }
    }
},
{
    "name": "spironolactone",
    "description": {
        "usage": {
            "short": "Used to treat fluid retention and high blood pressure.",
            "detailed": "Spironolactone is a potassium-sparing diuretic used to treat fluid retention and conditions like heart failure and high blood pressure."
        },
        "why_to_use": {
            "short": "Helps reduce swelling and blood pressure.",
            "detailed": "Spironolactone works by preventing the body from absorbing too much salt while keeping potassium levels steady."
        },
        "advantages": {
            "short": "Prevents potassium loss.",
            "detailed": "Unlike other diuretics, spironolactone helps maintain potassium levels in the body."
        },
        "disadvantages": {
            "short": "May cause breast enlargement in males.",
            "detailed": "Some users, particularly males, may experience breast enlargement as a side effect."
        },
        "side_effects": {
            "short": "Increased potassium, breast tenderness.",
            "detailed": "Side effects include elevated potassium levels, breast tenderness, and in rare cases, kidney dysfunction."
        }
    }
},
{
    "name": "famotidine",
    "description": {
        "usage": {
            "short": "Used to treat acid reflux and heartburn.",
            "detailed": "Famotidine is an H2 blocker that reduces stomach acid, relieving symptoms of heartburn and indigestion."
        },
        "why_to_use": {
            "short": "Helps reduce stomach acid effectively.",
            "detailed": "Famotidine provides relief from heartburn and acid reflux by decreasing the amount of acid the stomach produces."
        },
        "advantages": {
            "short": "Works quickly to relieve heartburn.",
            "detailed": "Famotidine starts working within an hour, offering quick relief from acid reflux and heartburn."
        },
        "disadvantages": {
            "short": "May cause headache and constipation.",
            "detailed": "Common side effects include headaches, constipation, and in rare cases, an increased risk of kidney issues."
        },
        "side_effects": {
            "short": "Headache, constipation.",
            "detailed": "Common side effects include headaches and constipation, with occasional dizziness."
        }
    }
},
{
    "name": "lansoprazole",
    "description": {
        "usage": {
            "short": "Used to treat stomach ulcers and GERD.",
            "detailed": "Lansoprazole is a proton pump inhibitor that reduces the amount of acid produced in the stomach, used to treat ulcers and gastroesophageal reflux disease (GERD)."
        },
        "why_to_use": {
            "short": "Reduces stomach acid effectively.",
            "detailed": "Lansoprazole is effective in treating acid-related conditions, providing long-term relief from ulcers and GERD."
        },
        "advantages": {
            "short": "Prolonged relief from heartburn.",
            "detailed": "Lansoprazole offers up to 24-hour relief from heartburn and acid reflux symptoms."
        },
        "disadvantages": {
            "short": "May take a few days to take effect.",
            "detailed": "Lansoprazole is not intended for immediate relief and may take 1-4 days to provide full symptom relief."
        },
        "side_effects": {
            "short": "Headache, nausea.",
            "detailed": "Common side effects include headaches, nausea, and in rare cases, low magnesium levels."
        }
    }
},
{
    "name": "hydroxyzine",
    "description": {
        "usage": {
            "short": "Used to treat anxiety and itching.",
            "detailed": "Hydroxyzine is an antihistamine that is used to treat anxiety, tension, and itching due to allergic reactions."
        },
        "why_to_use": {
            "short": "Helps relieve anxiety and itching.",
            "detailed": "Hydroxyzine is effective for both short-term anxiety management and relief from itching caused by allergies."
        },
        "advantages": {
            "short": "Non-addictive and works quickly.",
            "detailed": "Unlike benzodiazepines, hydroxyzine does not cause dependency and provides quick relief from anxiety."
        },
        "disadvantages": {
            "short": "Can cause drowsiness.",
            "detailed": "Common side effects include drowsiness, especially when taken during the day."
        },
        "side_effects": {
            "short": "Drowsiness, dry mouth.",
            "detailed": "Common side effects include drowsiness and dry mouth, particularly with higher doses."
        }
    }
},
{
    "name": "labetalol",
    "description": {
        "usage": {
            "short": "Used to treat high blood pressure.",
            "detailed": "Labetalol is a beta-blocker that reduces blood pressure by relaxing blood vessels and slowing heart rate."
        },
        "why_to_use": {
            "short": "Effective for managing high blood pressure.",
            "detailed": "Labetalol is commonly used to treat high blood pressure, particularly during pregnancy."
        },
        "advantages": {
            "short": "Effective in both oral and intravenous forms.",
            "detailed": "It can be used orally for long-term management or intravenously for emergencies."
        },
        "disadvantages": {
            "short": "May cause dizziness and fatigue.",
            "detailed": "Common side effects include dizziness, fatigue, and gastrointestinal discomfort."
        },
        "side_effects": {
            "short": "Dizziness, fatigue.",
            "detailed": "Common side effects include dizziness, fatigue, and shortness of breath."
        }
    }
},
{
    "name": "methotrexate",
    "description": {
        "usage": {
            "short": "Used to treat rheumatoid arthritis and cancer.",
            "detailed": "Methotrexate is an immunosuppressant used to treat autoimmune diseases like rheumatoid arthritis and some types of cancer."
        },
        "why_to_use": {
            "short": "Effective in controlling immune responses.",
            "detailed": "Methotrexate works by suppressing the immune system to prevent joint damage and control inflammation."
        },
        "advantages": {
            "short": "Effective for long-term management of autoimmune conditions.",
            "detailed": "It is widely used for long-term control of rheumatoid arthritis and psoriasis."
        },
        "disadvantages": {
            "short": "Can cause liver toxicity.",
            "detailed": "Methotrexate requires regular monitoring of liver function due to potential liver toxicity."
        },
        "side_effects": {
            "short": "Nausea, liver damage.",
            "detailed": "Side effects include nausea, fatigue, and risk of liver damage with long-term use."
        }
    }
},
{
    "name": "levetiracetam",
    "description": {
        "usage": {
            "short": "Used to treat seizures.",
            "detailed": "Levetiracetam is an anticonvulsant medication used to treat seizures in people with epilepsy."
        },
        "why_to_use": {
            "short": "Helps control seizures effectively.",
            "detailed": "Levetiracetam reduces the frequency of seizures and is used as part of an overall epilepsy treatment plan."
        },
        "advantages": {
            "short": "Well tolerated with fewer drug interactions.",
            "detailed": "Levetiracetam is often preferred due to its minimal interactions with other medications."
        },
        "disadvantages": {
            "short": "May cause mood changes.",
            "detailed": "Some patients report mood changes or irritability as a side effect."
        },
        "side_effects": {
            "short": "Fatigue, mood changes.",
            "detailed": "Common side effects include fatigue, irritability, and dizziness."
        }
    }
},
{
    "name": "tizanidine",
    "description": {
        "usage": {
            "short": "Used to treat muscle spasticity.",
            "detailed": "Tizanidine is a muscle relaxant used to treat muscle spasms caused by conditions such as multiple sclerosis and spinal cord injuries."
        },
        "why_to_use": {
            "short": "Effective for reducing muscle spasms.",
            "detailed": "Tizanidine helps relieve muscle spasms, allowing for improved mobility and reduced discomfort."
        },
        "advantages": {
            "short": "Short-acting muscle relaxant.",
            "detailed": "It provides quick relief for muscle spasms with a shorter duration of action compared to other muscle relaxants."
        },
        "disadvantages": {
            "short": "May cause drowsiness and low blood pressure.",
            "detailed": "Common side effects include drowsiness and hypotension, which may limit its use during the day."
        },
        "side_effects": {
            "short": "Drowsiness, low blood pressure.",
            "detailed": "Side effects include drowsiness, dizziness, and low blood pressure."
        }
    }
},
{
    "name": "venlafaxine",
    "description": {
        "usage": {
            "short": "Used to treat depression and anxiety.",
            "detailed": "Venlafaxine is a serotonin-norepinephrine reuptake inhibitor (SNRI) used to treat depression, anxiety, and panic disorders."
        },
        "why_to_use": {
            "short": "Improves mood and reduces anxiety.",
            "detailed": "Venlafaxine helps balance serotonin and norepinephrine levels, improving mood and reducing anxiety."
        },
        "advantages": {
            "short": "Effective for anxiety and panic disorders.",
            "detailed": "Venlafaxine is particularly effective in treating generalized anxiety disorder and social anxiety disorder."
        },
        "disadvantages": {
            "short": "May cause withdrawal symptoms.",
            "detailed": "Abrupt discontinuation can lead to withdrawal symptoms, including dizziness and irritability."
        },
        "side_effects": {
            "short": "Nausea, dry mouth.",
            "detailed": "Common side effects include nausea, dry mouth, and dizziness."
        }
    }
},
{
    "name": "prednisolone",
    "description": {
        "usage": {
            "short": "Used to treat inflammation and autoimmune conditions.",
            "detailed": "Prednisolone is a corticosteroid used to treat inflammatory and autoimmune diseases such as arthritis and asthma."
        },
        "why_to_use": {
            "short": "Reduces inflammation effectively.",
            "detailed": "Prednisolone works by suppressing the immune system to reduce inflammation and pain."
        },
        "advantages": {
            "short": "Effective for acute inflammation relief.",
            "detailed": "It is commonly used for short-term relief of inflammation in conditions like asthma flare-ups."
        },
        "disadvantages": {
            "short": "Long-term use can cause side effects.",
            "detailed": "Prolonged use of prednisolone can lead to side effects such as osteoporosis and weight gain."
        },
        "side_effects": {
            "short": "Weight gain, mood changes.",
            "detailed": "Side effects include increased appetite, weight gain, and mood changes."
        }
    }
},
{
    "name": "baclofen",
    "description": {
        "usage": {
            "short": "Used to treat muscle spasms.",
            "detailed": "Baclofen is a muscle relaxant used to relieve muscle spasms and stiffness associated with conditions like multiple sclerosis and spinal cord injuries."
        },
        "why_to_use": {
            "short": "Relieves muscle spasticity effectively.",
            "detailed": "Baclofen helps improve muscle mobility and reduces spasticity, improving quality of life for patients with neurological conditions."
        },
        "advantages": {
            "short": "Effective for long-term spasticity management.",
            "detailed": "It is commonly used for chronic muscle spasticity and has a well-established safety profile."
        },
        "disadvantages": {
            "short": "May cause drowsiness.",
            "detailed": "Baclofen is known to cause drowsiness, particularly when starting the medication."
        },
        "side_effects": {
            "short": "Drowsiness, dizziness.",
            "detailed": "Common side effects include drowsiness, dizziness, and muscle weakness."
        }
    }
},
{
    "name": "cephalexin",
    "description": {
        "usage": {
            "short": "Used to treat bacterial infections.",
            "detailed": "Cephalexin is a cephalosporin antibiotic used to treat various bacterial infections, including respiratory, ear, skin, and urinary tract infections."
        },
        "why_to_use": {
            "short": "Effective for treating common bacterial infections.",
            "detailed": "Cephalexin works by stopping the growth of bacteria, making it effective for a wide range of bacterial infections."
        },
        "advantages": {
            "short": "Well tolerated with a broad spectrum of action.",
            "detailed": "It is widely prescribed for both adults and children due to its broad effectiveness and safety profile."
        },
        "disadvantages": {
            "short": "May cause gastrointestinal upset.",
            "detailed": "Cephalexin can cause mild gastrointestinal side effects, including diarrhea and stomach cramps."
        },
        "side_effects": {
            "short": "Diarrhea, nausea.",
            "detailed": "Common side effects include diarrhea, nausea, and stomach discomfort."
        }
    }
},
{
    "name": "propranolol",
    "description": {
        "usage": {
            "short": "Used to treat high blood pressure and anxiety.",
            "detailed": "Propranolol is a beta-blocker that is used to manage high blood pressure, anxiety, and certain types of irregular heartbeats."
        },
        "why_to_use": {
            "short": "Effective for blood pressure control and anxiety reduction.",
            "detailed": "Propranolol helps reduce blood pressure, heart rate, and physical symptoms of anxiety."
        },
        "advantages": {
            "short": "Effective for performance anxiety and migraines.",
            "detailed": "It is commonly used for performance anxiety and migraine prevention due to its calming effects on the heart."
        },
        "disadvantages": {
            "short": "May cause fatigue and cold extremities.",
            "detailed": "Propranolol can cause tiredness and a feeling of cold in the extremities, particularly in high doses."
        },
        "side_effects": {
            "short": "Fatigue, dizziness.",
            "detailed": "Common side effects include fatigue, dizziness, and slow heart rate."
        }
    }
},
{
    "name": "valsartan",
    "description": {
        "usage": {
            "short": "Used to treat high blood pressure and heart failure.",
            "detailed": "Valsartan is an angiotensin II receptor blocker (ARB) that helps relax blood vessels, improving blood flow and reducing blood pressure."
        },
        "why_to_use": {
            "short": "Reduces the risk of heart disease.",
            "detailed": "Valsartan is used to manage high blood pressure, reducing the risk of heart attack, stroke, and heart failure."
        },
        "advantages": {
            "short": "Well tolerated with few side effects.",
            "detailed": "Valsartan is generally well tolerated and effective for long-term management of high blood pressure."
        },
        "disadvantages": {
            "short": "May cause dizziness and fatigue.",
            "detailed": "Some users experience dizziness, particularly when starting the medication."
        },
        "side_effects": {
            "short": "Dizziness, fatigue.",
            "detailed": "Side effects include dizziness, fatigue, and occasional kidney function changes."
        }
    }
},
{
    "name": "naproxen",
    "description": {
        "usage": {
            "short": "Used to treat pain and inflammation.",
            "detailed": "Naproxen is an NSAID (non-steroidal anti-inflammatory drug) commonly used to relieve pain from arthritis, muscle aches, and menstrual cramps."
        },
        "why_to_use": {
            "short": "Effective for reducing pain and inflammation.",
            "detailed": "Naproxen is effective in treating a variety of pain conditions by reducing inflammation and swelling."
        },
        "advantages": {
            "short": "Long-lasting pain relief.",
            "detailed": "Naproxen provides long-lasting relief from pain, often lasting up to 12 hours with a single dose."
        },
        "disadvantages": {
            "short": "Can cause stomach irritation with long-term use.",
            "detailed": "Prolonged use may lead to gastrointestinal side effects like ulcers or stomach bleeding."
        },
        "side_effects": {
            "short": "Nausea, stomach pain.",
            "detailed": "Common side effects include nausea, heartburn, and gastrointestinal discomfort."
        }
    }
},
{
    "name": "meloxicam",
    "description": {
        "usage": {
            "short": "Used to treat pain and inflammation.",
            "detailed": "Meloxicam is an NSAID used to treat pain or inflammation caused by osteoarthritis and rheumatoid arthritis."
        },
        "why_to_use": {
            "short": "Effective for arthritis-related pain.",
            "detailed": "Meloxicam helps reduce joint pain, stiffness, and swelling associated with arthritis."
        },
        "advantages": {
            "short": "Once-daily dosing for arthritis relief.",
            "detailed": "A single daily dose provides relief for most arthritis symptoms, making it convenient for long-term use."
        },
        "disadvantages": {
            "short": "May cause gastrointestinal issues.",
            "detailed": "Long-term use can lead to gastrointestinal problems like ulcers or bleeding, particularly in older adults."
        },
        "side_effects": {
            "short": "Stomach pain, dizziness.",
            "detailed": "Common side effects include stomach upset, dizziness, and diarrhea."
        }
    }
},
{
    "name": "hydroxychloroquine",
    "description": {
        "usage": {
            "short": "Used to treat malaria and autoimmune diseases.",
            "detailed": "Hydroxychloroquine is used to prevent and treat malaria, as well as to treat autoimmune diseases like lupus and rheumatoid arthritis."
        },
        "why_to_use": {
            "short": "Effective for autoimmune disease management.",
            "detailed": "Hydroxychloroquine helps control the immune system, reducing inflammation in autoimmune conditions."
        },
        "advantages": {
            "short": "Widely used for lupus and arthritis.",
            "detailed": "It is often prescribed for long-term management of lupus and rheumatoid arthritis due to its immunosuppressive effects."
        },
        "disadvantages": {
            "short": "Requires regular eye exams.",
            "detailed": "Long-term use can cause vision problems, so regular eye exams are necessary to monitor for potential retinal damage."
        },
        "side_effects": {
            "short": "Nausea, blurred vision.",
            "detailed": "Common side effects include nausea, diarrhea, and, in rare cases, vision disturbances."
        }
    }
},
{
    "name": "rivastigmine",
    "description": {
        "usage": {
            "short": "Used to treat dementia.",
            "detailed": "Rivastigmine is a cholinesterase inhibitor used to treat symptoms of dementia in Alzheimer's and Parkinson's disease."
        },
        "why_to_use": {
            "short": "Helps manage cognitive decline.",
            "detailed": "Rivastigmine works by increasing levels of acetylcholine, a chemical important for memory and cognition, helping slow cognitive decline."
        },
        "advantages": {
            "short": "Can improve memory and daily function.",
            "detailed": "It is commonly prescribed to improve cognitive function and daily living in patients with mild to moderate dementia."
        },
        "disadvantages": {
            "short": "May cause gastrointestinal discomfort.",
            "detailed": "Nausea, vomiting, and loss of appetite are common side effects, particularly at higher doses."
        },
        "side_effects": {
            "short": "Nausea, vomiting.",
            "detailed": "Side effects include gastrointestinal discomfort, dizziness, and headaches."
        }
    }
},
{
    "name": "lamotrigine",
    "description": {
        "usage": {
            "short": "Used to treat epilepsy and bipolar disorder.",
            "detailed": "Lamotrigine is an anticonvulsant medication used to prevent seizures and stabilize mood in people with bipolar disorder."
        },
        "why_to_use": {
            "short": "Effective for mood stabilization and seizure control.",
            "detailed": "Lamotrigine helps control seizures and prevent mood swings in bipolar patients."
        },
        "advantages": {
            "short": "Dual benefits for mood and seizures.",
            "detailed": "It is commonly prescribed for both seizure control and mood stabilization, offering dual benefits."
        },
        "disadvantages": {
            "short": "May cause serious skin rashes.",
            "detailed": "Rare but severe side effects include life-threatening skin rashes, such as Stevens-Johnson syndrome."
        },
        "side_effects": {
            "short": "Dizziness, blurred vision.",
            "detailed": "Common side effects include dizziness, double vision, and headaches."
        }
    }
},
{
    "name": "gabapentin",
    "description": {
        "usage": {
            "short": "Used to treat nerve pain and seizures.",
            "detailed": "Gabapentin is an anticonvulsant used to relieve nerve pain from shingles and to treat seizures."
        },
        "why_to_use": {
            "short": "Helps control nerve pain and seizures.",
            "detailed": "Gabapentin alters the way the body senses pain, particularly from nerve damage, and helps control seizures."
        },
        "advantages": {
            "short": "Effective for nerve pain relief.",
            "detailed": "Gabapentin is widely prescribed for its effectiveness in treating neuropathic pain."
        },
        "disadvantages": {
            "short": "May cause drowsiness and dizziness.",
            "detailed": "Gabapentin can cause significant drowsiness and dizziness, particularly when first starting treatment."
        },
        "side_effects": {
            "short": "Drowsiness, dizziness.",
            "detailed": "Common side effects include drowsiness, dizziness, and coordination problems."
        }
    }
},
{
    "name": "zolpidem",
    "description": {
        "usage": {
            "short": "Used to treat insomnia.",
            "detailed": "Zolpidem is a sedative used to treat sleep disorders like insomnia, helping patients fall asleep faster and stay asleep longer."
        },
        "why_to_use": {
            "short": "Effective for short-term sleep aid.",
            "detailed": "Zolpidem helps patients with insomnia by increasing sleep duration and reducing the time it takes to fall asleep."
        },
        "advantages": {
            "short": "Fast-acting sleep aid.",
            "detailed": "Zolpidem acts quickly, usually helping patients fall asleep within 15-30 minutes."
        },
        "disadvantages": {
            "short": "Can cause dependence with long-term use.",
            "detailed": "Zolpidem can cause dependence if used for prolonged periods, and it is typically prescribed for short-term use."
        },
        "side_effects": {
            "short": "Drowsiness, dizziness.",
            "detailed": "Common side effects include next-day drowsiness, dizziness, and headaches."
        }
    }
},
{
    "name": "donepezil",
    "description": {
        "usage": {
            "short": "Used to treat dementia.",
            "detailed": "Donepezil is a cholinesterase inhibitor that improves cognitive function in people with Alzheimer's disease by increasing acetylcholine levels in the brain."
        },
        "why_to_use": {
            "short": "Helps improve memory and daily function.",
            "detailed": "Donepezil is commonly prescribed to slow memory loss and cognitive decline in Alzheimer's patients."
        },
        "advantages": {
            "short": "Improves cognitive function in Alzheimer's patients.",
            "detailed": "Donepezil helps improve memory, awareness, and the ability to perform daily tasks in people with dementia."
        },
        "disadvantages": {
            "short": "May cause gastrointestinal issues.",
            "detailed": "Side effects include nausea, diarrhea, and loss of appetite, especially at higher doses."
        },
        "side_effects": {
            "short": "Nausea, diarrhea.",
            "detailed": "Common side effects include nausea, diarrhea, and dizziness."
        }
    }
},
{
    "name": "ondansetron",
    "description": {
        "usage": {
            "short": "Used to prevent nausea and vomiting.",
            "detailed": "Ondansetron is an antiemetic used to prevent nausea and vomiting caused by surgery, chemotherapy, or radiation therapy."
        },
        "why_to_use": {
            "short": "Effective in preventing nausea.",
            "detailed": "Ondansetron blocks the actions of chemicals in the body that trigger nausea and vomiting."
        },
        "advantages": {
            "short": "Highly effective for nausea prevention.",
            "detailed": "Ondansetron is widely prescribed for its effectiveness in preventing nausea and vomiting, particularly in cancer patients."
        },
        "disadvantages": {
            "short": "May cause headaches and constipation.",
            "detailed": "Side effects include headaches, constipation, and, in rare cases, irregular heartbeat."
        },
        "side_effects": {
            "short": "Headaches, constipation.",
            "detailed": "Common side effects include headaches, constipation, and dizziness."
        }
    }
},
{
    "name": "fentanyl",
    "description": {
        "usage": {
            "short": "Used to treat severe pain.",
            "detailed": "Fentanyl is a potent opioid analgesic used to treat severe pain, often in patients with cancer or after surgery."
        },
        "why_to_use": {
            "short": "Effective for managing severe pain.",
            "detailed": "Fentanyl is one of the strongest painkillers available, providing relief for patients with extreme pain."
        },
        "advantages": {
            "short": "Very potent and fast-acting.",
            "detailed": "Fentanyl works quickly and effectively to relieve severe pain, making it suitable for critical care."
        },
        "disadvantages": {
            "short": "High risk of addiction and overdose.",
            "detailed": "Fentanyl carries a high risk of abuse, dependence, and overdose, requiring careful medical supervision."
        },
        "side_effects": {
            "short": "Drowsiness, constipation.",
            "detailed": "Common side effects include drowsiness, constipation, and nausea."
        }
    }
}


]

# Insert medicines into the collection
medicines_collection.insert_many(medicines_data)
print("Medicines added successfully.")
