# 癌症负担与发展水平：全球健康不平等研究
癌症作为恶性细胞不受控增殖的致命性疾病，已成为全球第二大死因。据国际癌症研究机构（IARC）最新统计，2023年全球新发癌症病例突破2000万例，相当于每1.6秒就有一人被确诊；死亡病例高达970万例，超过艾滋病、结核病和疟疾死亡人数的总和。其危害不仅体现在个体层面——患者五年生存率在低收入国家不足30%，更深刻重塑着社会发展轨迹：癌症相关生产力损失导致全球经济年损耗超1.2万亿美元，相当于印尼全年GDP总量。癌症作为非传染性疾病中的首要死因，其全球分布呈现与经济发展水平密切相关的“梯度不平等”特征。基于世界银行收入分组（高收入、中高收入、低收入）的流行病学数据揭示，癌症负担在发病率、死亡率和癌谱构成三个维度均存在系统性差异。尤为严峻的是，这种负担分布极不均衡——占全球人口84%的中低收入国家承担着71%的癌症死亡，却仅获得5%的防控资源。癌症防控已超越医学范畴，成为检验人类文明发展伦理的试金石。
以下，基于Kaggle网站所提供的全球过去一段时间内的癌症数据，对一些代表性国家不同年龄段患病率等进行了分析。并且尝试不同国家的发展水平与患病率之间的关系。

统计了1990-2015年之间，死于各种癌症的总人数，列举出了前六种最主要的癌症类型（Fig.1）。其中，肺癌是头号“杀手”， 死亡人数 遥遥领先，达到惊人的 36,962,830 例，远高于其他癌症，死亡人数几乎是第二名胃癌（22,637,244 例）的 1.6倍。前六名中，四种（胃癌、结直肠癌、食管癌、肝癌）属于消化道癌症（胃、肠、食道、肝）。死亡总数为：22,637,244 (胃) + 18,720,287 (结直肠) + 10,697,539 (食管) + 10,693,552 (肝) = 62,748,600 例，远超过排名第四的乳腺癌（约 1288 万例），强调了消化系统癌症整体负担之重。

![image](https://github.com/user-attachments/assets/d033ec6c-2849-4a9a-aa72-6b38cc7cdcdb)


之后，我好奇，不同发展水平国家不同年龄段的患癌率是怎么样的，根据得到的数据，我挑选了八个比较比较有代表性的国家，发达国家（美国，日本，德国），发展中国家（中国，墨西哥，伊朗，印度，埃塞俄比亚），分别计算了他们各个年龄段的患病率（Fig.2,Fig.3）。我发现，发达国家发病率随年龄急剧上升，70+岁人群占比超过50%（日德尤为突出），这可能与他们的人口老龄化问题有直接关联，青壮年（15-49岁）比例极低（<10%）。发展中国家年龄分布更加分散，老年组占比低于发达国家。

![image](https://github.com/user-attachments/assets/b0f42c4c-5029-4dac-a022-fe1b3a019019)



![image](https://github.com/user-attachments/assets/6935f05d-7d33-4957-ac7b-2ec4ced2dd5f)

既然发现美国德国日本这些发达国家70+以上的患病率比较高，我根据2015年的数据对全球各个国家70+的患病率都做了分析（Fig.4），确实以美国，加拿大，澳大利这写发达国家70+以上的发病率在世界范围内是比较高的。

![image](https://github.com/user-attachments/assets/53404d75-65cb-4260-a9e2-6debf316605b)

根据上面看到一些结论，我想知道一个国家越发达，青少年患病率越低，老年人患病率越高这样的结论是不是正确的，我根据2015年各个国家的人均GDP，将国家分成三个组别，来计算和各个年龄段发病率之间的相关性（Fig.5）。年轻群体（Under5, 5-14y），在所有收入组均呈现负相关（蓝色），尤其是高收入国家的5岁以下儿童（-0.50）。表明，经济越发达，儿童癌症死亡率越低，反映先进的儿童癌症筛查、疫苗普及和医疗可及性。
老年群体（70+y）：为正相关（红色），中高收入组最显著（0.20），经济发达地区人口寿命延长，老年癌症病例增加。高收入国家，15-49岁群体负相关也很强（-0.36），高GDP支撑壮年群体癌症预防体系（如乳腺癌/前列腺癌筛查）。对于中低收入国家，50-69岁群体无相关性（-0.01），经济因素对中年癌症防治影响微弱，医疗资源不足是主因。
70岁是转折年龄：所有组别在该年龄段后，GDP与死亡率关系由负转正. 中高收入国家在5-14y→15-49y阶段出现剧烈反转（0.01→-0.06→0.14） 反映该收入层医疗系统存在特定年龄段的资源断层。

![image](https://github.com/user-attachments/assets/e7920a6d-9108-454c-886c-4a06bf6d9fcb)


经济发展对癌症防治的影响具有年龄敏感性和收入层级效应。高GDP在降低年轻群体癌症死亡率方面效果显著，但伴随人口老龄化，经济红利会转变为老年癌症负担。中高收入国家正处于防治体系转型关键期，需警惕青少年至壮年群体的癌症风险抬头。








