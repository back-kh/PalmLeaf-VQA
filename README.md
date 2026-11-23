# PalmLeaf-VQA

**📍 WACV 2027 Disney Springs, Florida, USA**

🎉 **Accepted in the first round.**

**PalmLeaf-VQA: A Multi-Script Visual Question Answering Benchmark for Historical Palm-Leaf Manuscript Understanding Across Diverse Regions**

**Project lead: Nimol Thuon**

[🌐 Project webpage](https://back-kh.github.io/palmleaf-vqa/) | [📄 Read the preprint](https://arxiv.org/abs/2609.31651) | [Test set on Hugging Face](https://huggingface.co/datasets/Backkh/PalmLeaf-VQA) | [🗺️ Project roadmap](#roadmap) | [📖 Citation](#citation)

## 🔎 Overview

PalmLeaf-VQA is a visual question answering benchmark for historical palm-leaf manuscript images from South and Southeast Asian collections. It evaluates observable manuscript properties, including physical condition, visible line structure, symbols and drawings, material-related attributes, binding holes, and margins.

The benchmark focuses on manuscript layout and physical attributes. It does not evaluate full-text transcription, translation, or understanding of the manuscripts' textual content.

## 🖼️ Benchmark Overview

![Figure 1. PalmLeaf-VQA overview showing eight manuscript collections, example visual question-answer pairs, eight question categories, and five task types.](assets/fig1-overview-corrected.png)

*Figure 1 adapted from the [paper](https://arxiv.org/abs/2609.31651), with the Grantha example question corrected to "What other visible physical feature is present?" to match its answer and category. The overview presents representative manuscript collections and QA examples, the question taxonomy, and five task types: classification, counting, layout reasoning, binary recognition, and attribute recognition.*

## 📌 Current Status

**WACV 2027 accepted.** The [project webpage](https://back-kh.github.io/palmleaf-vqa/) is live, and the reviewed test set is publicly available on [Hugging Face](https://huggingface.co/datasets/Backkh/PalmLeaf-VQA) for **non-commercial use only**. The [test ZIP](https://huggingface.co/datasets/Backkh/PalmLeaf-VQA/resolve/main/PalmLeaf-VQA-Test-Images-QA.zip) contains **278 manuscript image records** and **2,224 approved question-answer pairs**.

### 📰 News

- **November 24, 2026:** [New evaluations](#model-benchmarks-new-evaluations) for six models are available under open and constrained prompting.
- **November 23, 2026:** The [project webpage](https://back-kh.github.io/palmleaf-vqa/) went live and the [test dataset](https://huggingface.co/datasets/Backkh/PalmLeaf-VQA) was released.
- **WACV 2027:** PalmLeaf-VQA has been accepted in the first round.
- **September 14, 2026:** The first [preprint](https://arxiv.org/abs/2609.31651) became available on arXiv.

## Roadmap

| Step | Milestone | Status | Details |
| --- | --- | --- | --- |
| 1 | First preprint published | ✅ Complete | Paper available on arXiv. |
| 2 | WACV 2027 acceptance | ✅ Complete | Accepted in the first round. |
| 3 | Project webpage launch | ✅ Complete | The [project webpage](https://back-kh.github.io/palmleaf-vqa/) is live with examples, paper results, and download links. |
| 4 | Test dataset release | ✅ Complete | Test images and reviewed QA are available on [Hugging Face](https://huggingface.co/datasets/Backkh/PalmLeaf-VQA) for non-commercial use only. |
| 5 | Paper benchmark evaluation | ✅ Complete | The [paper's model performance tables](https://arxiv.org/html/2609.31651v1#S5) report test-set results without task-specific fine-tuning. |
| 6 | Full benchmark paper and materials | ✅ Complete | The [preprint and supplement](https://arxiv.org/html/2609.31651v1) include the benchmark tables and evaluation protocol. |
| 7 | Newer-model benchmark updates | ✅ Published | [Results for six additional models](#model-benchmarks-new-evaluations) are available separately from the paper. |
| 8 | Training and validation release and follow-up benchmark | ⏳ Planned | Release training and validation annotations, split identifiers, and access instructions. Use training data for fine-tuning and validation data for model selection, then check for overlap before evaluating on the test set. |

Release links and completion dates will be added here as each milestone is reached. Planned milestones are not announcements of completed releases.

## 📊 Benchmark at a Glance

As described in the paper, PalmLeaf-VQA contains **923 manuscript images** and **7,384 question-answer pairs**, with eight questions per image across eight categories.

| Split | Images | Question-answer pairs |
| --- | ---: | ---: |
| Train | 553 | 4,424 |
| Validation | 92 | 736 |
| Test | 278 | 2,224 |
| **Total** | **923** | **7,384** |

The split counts refer to manuscript image records.

## Model Benchmarks (New evaluations)

These follow-up results are separate from the accepted paper. See also the [project webpage benchmark table](https://back-kh.github.io/palmleaf-vqa/#new-evaluations).

| Model | Mode | Exact acc. | Mean F1 | Mean Jaccard |
| --- | --- | ---: | ---: | ---: |
| deepseek4.1-flash | Constrained | 48.92% | 53.25% | 51.67% |
| deepseek4.1-flash | Open | 27.70% | 28.18% | 28.06% |
| qwen3.8-flash-next | Constrained | 49.91% | 56.72% | 54.63% |
| qwen3.8-flash-next | Open | 32.37% | 32.58% | 32.50% |
| glm-5.3-flash | Constrained | 48.02% | 54.55% | 52.52% |
| glm-5.3-flash | Open | 34.44% | 34.55% | 34.51% |
| qwen3.8-27B | Constrained | 44.38% | 49.51% | 47.72% |
| qwen3.8-27B | Open | 34.76% | 34.77% | 34.77% |
| GPT-6.2 Sol (Max) | Constrained | 62.37% | 73.87% | 71.53% |
| GPT-6.2 Sol (Max) | Open | 46.27% | 48.07% | 47.36% |
| GPT-6.2 Astra (Max) | Constrained | 59.22% | 69.72% | 67.54% |
| GPT-6.2 Astra (Max) | Open | 48.04% | 49.75% | 49.07% |

The GPT-6.2 Max runs used the archived WACV prompts and original test labels via Codex CLI, rather than the paper's API runner. Sol scored 2,224 answers per mode. Astra scored 2,224 constrained and 2,221 open answers; three open script-identification requests timed out and were excluded. The other four models' scores are reported as supplied.

## Python Quick Start

Download the [test-set ZIP](https://huggingface.co/datasets/Backkh/PalmLeaf-VQA/resolve/main/PalmLeaf-VQA-Test-Images-QA.zip) and run the [Python example](examples/inspect_test_set.py) from this repository. It uses only the Python standard library and reads annotations directly from the archive.

```bash
python3 examples/inspect_test_set.py PalmLeaf-VQA-Test-Images-QA.zip
python3 examples/inspect_test_set.py PalmLeaf-VQA-Test-Images-QA.zip --image Khmer_0009.jpg
```

The first command shows counts by collection. The second prints the selected image's question-answer pairs and its path inside the ZIP.

## 🌏 Scripts and Collections

PalmLeaf-VQA covers the following eight script/collection groups:

| Script / collection group | Images | Question-answer pairs |
| --- | ---: | ---: |
| Balinese | 100 | 800 |
| Grantha | 70 | 560 |
| Jathakam | 99 | 792 |
| Kambaramayanam | 80 | 640 |
| Kannada | 257 | 2,056 |
| Khmer | 155 | 1,240 |
| Sundanese | 61 | 488 |
| Tamil | 101 | 808 |
| **Total** | **923** | **7,384** |

These names identify source collections or manuscript traditions and do not necessarily correspond one-to-one to distinct scripts. Counts reflect the benchmark described in the paper.

## 🧾 Release and Evaluation Notes

- The test dataset is for **non-commercial use only**. Training and validation data are not yet released.
- Image access and redistribution will follow the original sources' terms. Restricted-source material will require source identifiers and retrieval instructions rather than unauthorized image redistribution.
- Annotation corrections and benchmark updates will be versioned. Results reported in the paper belong to the annotation version used for those experiments; corrected test labels require rescoring before results can be associated with the revised version.
- Future evaluations will document model versions, prompts, decoding settings, and scoring rules. New results will be distinguished from those reported in the accepted paper.

## Citation

Until the proceedings version is available, please cite the preprint:

```bibtex
@misc{thuon2026palmleafvqa,
  title={PalmLeaf-VQA: A Multi-Script Visual Question Answering Benchmark for Historical Palm-Leaf Manuscript Understanding Across Diverse Regions},
  author={Nimol Thuon and Jun Du and Panhapin Theang},
  year={2026},
  eprint={2609.31651},
  archivePrefix={arXiv},
  primaryClass={cs.CV},
  url={https://arxiv.org/abs/2609.31651}
}
```

## 📬 Contact

For questions about the benchmark and planned releases, contact **Nimol Thuon** at [nimol.thuon@gmail.com](mailto:nimol.thuon@gmail.com).

*Last updated: November 24, 2026.*
