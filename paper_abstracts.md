# Paper Abstracts

This file collects concise paper abstracts for the papers tracked in this repository, so we can quickly understand each paper before opening the full PDF or source files.

## Embodied Robotics

### GR-1

**Paper:** [Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation](docs/papers/embodied_robotics/20231220_unleashing_large_scale_video_generative_pre_training_for_visual_robot_manipulation/paper_arxiv_code/README.md)  
**arXiv:** [2312.13139](https://arxiv.org/abs/2312.13139)

**Abstract:**  
This paper shows that large-scale video generative pre-training can substantially improve visual robot manipulation. It proposes GR-1, a GPT-style language-conditioned robot model that takes instructions, image sequences, and robot states as input, and jointly predicts robot actions and future images in an end-to-end way. After pretraining on large video data and finetuning on robot trajectories, GR-1 achieves strong gains on CALVIN and real-robot evaluation, especially in zero-shot generalization to unseen scenes and objects.

### GR-2

**Paper:** [GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation](docs/papers/embodied_robotics/20241008_gr_2_a_generative_video_language_action_model_with_web_scale_knowledge_for_robot_manipulation/paper_arxiv_code/README.md)  
**arXiv:** [2410.06158](https://arxiv.org/abs/2410.06158)

**Abstract:**  
GR-2 is a generalist robot agent that first pretrains on massive internet video data to learn world dynamics, then finetunes on robot trajectories for both video generation and action prediction. The model is trained at web scale, using millions of video clips and tens of billions of tokens, and shows strong multi-task manipulation performance across more than 100 tasks. The paper emphasizes that large-scale video pretraining improves both task performance and generalization to novel environments, objects, and backgrounds.

### VidMan

**Paper:** [VidMan: Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation](docs/papers/embodied_robotics/20241114_vidman_exploiting_implicit_dynamics_from_video_diffusion_model_for_effective_robot_manipulation/paper_arxiv_code/README.md)  
**arXiv:** [2411.09153](https://arxiv.org/abs/2411.09153)

**Abstract:**  
VidMan uses a two-stage training recipe to turn a video diffusion backbone into an inverse dynamics model for robot control. First, it pretrains on large-scale robot trajectories for future visual prediction so the model learns implicit environment dynamics. Then it adds a lightweight adapter to predict actions from that dynamics-aware representation, improving data efficiency and manipulation accuracy on CALVIN and OXE benchmarks.

### PAD

**Paper:** [Prediction with Action: Visual Policy Learning via Joint Denoising Process](docs/papers/embodied_robotics/20241127_prediction_with_action_visual_policy_learning_via_joint_denoising_process/paper_arxiv_code/README.md)  
**arXiv:** [2411.18179](https://arxiv.org/abs/2411.18179)

**Abstract:**  
PAD unifies future image prediction and robot action generation inside one shared denoising process. Using Diffusion Transformers, it jointly models images, robot states, and actions so that video prediction and policy learning can reinforce each other through their shared physical dynamics. The method supports co-training on robot demonstrations and large-scale video data, and the paper reports strong improvements on Metaworld and real-world manipulation generalization.

### VPP

**Paper:** [Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations](docs/papers/embodied_robotics/20241219_video_prediction_policy_a_generalist_robot_policy_with_predictive_visual_representations/paper_arxiv_code/README.md)  
**arXiv:** [2412.14803](https://arxiv.org/abs/2412.14803)

**Abstract:**  
VPP argues that predictive representations from video diffusion models capture not only the current scene but also future dynamics that are crucial for robot control. It learns an implicit inverse dynamics policy conditioned on predicted future visual representations inside a video model, and fine-tunes the video foundation model on robot and internet manipulation data. The paper reports strong gains on CALVIN and real-world dexterous manipulation, suggesting that future-aware visual priors can substantially improve generalist robot policies.

### UVA

**Paper:** [Unified Video Action Model](docs/papers/embodied_robotics/20250228_unified_video_action_model/paper_arxiv_code/README.md)  
**arXiv:** [2503.00200](https://arxiv.org/abs/2503.00200)

**Abstract:**  
UVA unifies video generation and action prediction inside one robotics model. It learns a joint video-action latent space and uses lightweight decoupled heads so action inference can stay fast without generating future video at test time. The same model can also be trained with masked inputs to support forward dynamics, inverse dynamics, and video prediction, making it a flexible general-purpose robotics foundation model.

### DyWA

**Paper:** [DyWA: Dynamics-adaptive World Action Model for Generalizable Non-prehensile Manipulation](docs/papers/embodied_robotics/20250321_dywa_dynamics_adaptive_world_action_model_for_generalizable_non_prehensile_manipulation/paper_arxiv_code/README.md)  
**arXiv:** [2503.16806](https://arxiv.org/abs/2503.16806)

**Abstract:**  
DyWA targets non-prehensile manipulation under changing physical conditions such as object mass and table friction. The paper proposes a Dynamics-Adaptive World Action Model that jointly predicts future states while adapting to dynamics variations from historical trajectories, unifying geometry, state, physics, and robot actions. This improves robustness under partial observability and yields strong gains in both simulation and real-world manipulation experiments.

### AdaWorld

**Paper:** [AdaWorld: Learning Adaptable World Models with Latent Actions](docs/papers/embodied_robotics/20250324_adaworld_learning_adaptable_world_models_with_latent_actions/paper_arxiv_code/README.md)  
**arXiv:** [2503.18938](https://arxiv.org/abs/2503.18938)

**Abstract:**  
AdaWorld treats latent actions as the bridge between video prediction and action-conditioned world modeling. It learns adaptable world models by extracting latent actions from video in a self-supervised way, then conditioning an autoregressive dynamics model on those latent transitions. This makes it easier to transfer world models to new actions and environments with limited interaction data.

### UWM

**Paper:** [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](docs/papers/embodied_robotics/20250403_unified_world_models_coupling_video_and_action_diffusion_for_pretraining_on_large_robotic_datasets/paper_arxiv_code/README.md)  
**arXiv:** [2504.02792](https://arxiv.org/abs/2504.02792)

**Abstract:**  
Unified World Models couples video diffusion and action diffusion inside one transformer, with separate diffusion timesteps controlling each modality. This lets the same model behave as a policy, forward model, inverse model, or video generator, while also learning from action-free videos alongside robot trajectories. The paper frames this as a simple way to unify imitation learning and world modeling, and shows that the resulting pretrained policies become more robust and generalizable.

### Motus

**Paper:** [Motus: A Unified Latent Action World Model](docs/papers/embodied_robotics/20251215_motus_a_unified_latent_action_world_model/paper_arxiv_code/README.md)  
**arXiv:** [2512.13030](https://arxiv.org/abs/2512.13030)

**Abstract:**  
Motus proposes a unified latent action world model that combines understanding, video generation, and action prediction into one shared framework. It uses a Mixture-of-Transformer architecture together with a scheduler that can switch among multiple modes such as world modeling, VLA, inverse dynamics, video generation, and joint video-action prediction. By learning latent actions from optical flow and scaling pretraining across diverse data, Motus aims to unify embodied modeling capabilities and improve downstream robot control.

### mimic-video

**Paper:** [mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs](docs/papers/embodied_robotics/20251217_mimic_video_video_action_models_for_generalizable_robot_control_beyond_vlas/paper_arxiv_code/README.md)  
**arXiv:** [2512.15692](https://arxiv.org/abs/2512.15692)

**Abstract:**  
mimic-video argues that VLA models learn semantics well but remain weak on physical causality because they are pretrained mostly on static image-text data. It instead pairs a pretrained internet-scale video model with an action decoder that maps video-space action plans into low-level robot actions. The result is a Video-Action Model that improves both sample efficiency and convergence speed, while achieving strong generalization on simulated and real-world manipulation tasks.

### Cosmos Policy

**Paper:** [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](docs/papers/embodied_robotics/20260122_cosmos_policy_fine_tuning_video_models_for_visuomotor_control_and_planning/paper_arxiv_code/README.md)  
**arXiv:** [2601.16163](https://arxiv.org/abs/2601.16163)

**Abstract:**  
Cosmos Policy adapts a large pretrained video generation model into a robot policy through a single stage of post-training, without adding extra policy-specific architecture. It directly represents robot actions, future states, and values as latent frames inside the video diffusion process, which enables both visuomotor control and test-time planning. The paper reports strong results on simulation benchmarks and real-world bimanual manipulation, showing that video-model priors can be used for both policy execution and model-based planning.

### LingBot-VA

**Paper:** [Causal World Modeling for Robot Control](docs/papers/embodied_robotics/20260129_causal_world_modeling_for_robot_control/paper_arxiv_code/README.md)  
**arXiv:** [2601.21998](https://arxiv.org/abs/2601.21998)

**Abstract:**  
This paper presents LingBot-VA, a framework that treats video world modeling as a core foundation for robot control rather than just an auxiliary prediction task. It jointly learns frame prediction and policy execution in an autoregressive diffusion framework with a shared latent space for vision and action, a closed-loop rollout mechanism, and an asynchronous inference pipeline. The main claim is that causal video world modeling can serve as an efficient and generalizable basis for long-horizon robot behavior.

### DreamZero

**Paper:** [World Action Models are Zero-shot Policies](docs/papers/embodied_robotics/20260217_world_action_models_are_zero_shot_policies/paper_arxiv_code/README.md)  
**arXiv:** [2602.15922](https://arxiv.org/abs/2602.15922)

**Abstract:**  
State-of-the-art Vision-Language-Action (VLA) models excel at semantic generalization but struggle to generalize to unseen physical motions in novel environments. DreamZero introduces a World Action Model built on a pretrained video diffusion backbone, jointly modeling future video and actions so that heterogeneous robot data can be used more effectively. The paper reports over 2x improvement in generalization to new tasks and environments over strong VLA baselines, along with real-time closed-loop control at 7Hz and cross-embodiment transfer from short video-only demonstrations.

### Fast-WAM

**Paper:** [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](docs/papers/embodied_robotics/20260317_fast_wam_do_world_action_models_need_test_time_future_imagination/paper_arxiv_code/README.md)  
**arXiv:** [2603.16666](https://arxiv.org/abs/2603.16666)

**Abstract:**  
Fast-WAM studies whether world action models really need to generate future video during inference. It keeps video co-training during training, but removes explicit future imagination at test time, so the policy can act directly from the learned representation. The main finding is that training-time video modeling matters more than expensive test-time rollout, and the resulting model stays competitive while running much faster.

### GigaWorld-Policy

**Paper:** [GigaWorld-Policy: An Efficient Action-Centered World-Action Model](docs/papers/embodied_robotics/20260318_gigaworld_policy_an_efficient_action_centered_world_action_model/paper_arxiv_code/README.md)  
**arXiv:** [2603.17240](https://arxiv.org/abs/2603.17240)

**Abstract:**  
GigaWorld-Policy argues that existing world-action models suffer from heavy inference cost and entangled visual-motion reasoning. It proposes an action-centered WAM that predicts future action sequences directly and optionally generates future videos as an auxiliary training signal. With a causal design that prevents future video tokens from influencing action tokens, the model can skip explicit video generation at inference time, leading to much faster deployment while still improving real-world robotic performance.

### Action Images

**Paper:** [Action Images: End-to-End Policy Learning via Multiview Video Generation](docs/papers/embodied_robotics/20260407_action_images_end_to_end_policy_learning_via_multiview_video_generation/paper_arxiv_code/README.md)  
**arXiv:** [2604.06168](https://arxiv.org/abs/2604.06168)

**Abstract:**  
Action Images formulates robot policy learning as multiview video generation. Instead of using low-dimensional control tokens, it converts 7-DoF actions into pixel-grounded action images that explicitly track robot-arm motion across views. This lets the pretrained video backbone itself serve as a zero-shot policy without requiring a separate policy head, while also unifying action labeling, action-conditioned video generation, and joint video-action generation under one representation.

## Autonomous Driving

### DriveVA

**Paper:** [DriveVA: Video Action Models are Zero-Shot Drivers](docs/papers/autonomous_driving/20260405_driveva_video_action_models_are_zero_shot_drivers/paper_arxiv_code/README.md)  
**arXiv:** [2604.04198](https://arxiv.org/abs/2604.04198)

**Abstract:**  
DriveVA studies autonomous driving through a video-action world model that jointly generates future scene videos and action trajectories in one shared latent process. Instead of treating visual forecasting and planning as loosely coupled modules, it uses a DiT-based decoder to align trajectory planning with future scene evolution more tightly. By inheriting priors from large-scale video generation models, DriveVA improves generalization across unseen domains and sensor setups, and shows strong zero-shot driving performance on NAVSIM, nuScenes, and Bench2Drive.
