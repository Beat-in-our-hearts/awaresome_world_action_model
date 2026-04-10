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

### World2Act

**Paper:** [World2Act: Latent Action Post-Training via Skill-Compositional World Models](docs/papers/embodied_robotics/20260311_world2act_latent_action_post_training_via_skill_compositional_world_models/paper_arxiv_code/README.md)  
**arXiv:** [2603.10422](https://arxiv.org/abs/2603.10422)

**Abstract:**  
World2Act studies how world models can post-train VLA policies for better robustness and generalization under environmental shifts. Instead of supervising directly in pixel space, it aligns policy actions with world-model video-dynamics latents using a contrastive matching objective, which reduces sensitivity to rollout artifacts and hallucinated pixels. To handle long and variable-horizon robotic execution, it also introduces an LLM-based skill decomposition pipeline that breaks high-level instructions into lower-level prompts, enabling skill-compositional world models to stay temporally consistent across tasks. The result is a mainline embodied WAM paper centered on world-model-guided robot policy improvement rather than only latent-action pretraining.

### S-VAM

**Paper:** [S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight](docs/papers/embodied_robotics/20260317_s_vam_shortcut_video_action_model_by_self_distilling_geometric_and_semantic_foresight/paper_arxiv_code/README.md)  
**arXiv:** [2603.16195](https://arxiv.org/abs/2603.16195)

**Abstract:**  
S-VAM targets the efficiency bottleneck in robot video-action models. Rather than relying on slow multi-step video rollout or noisy one-step features, it distills the geometric and semantic foresight of a multi-step diffusion model into a single forward pass, so the policy can act from a cleaner and faster predictive blueprint. The paper keeps the core VAM setting, using future-aware visual representations to simplify downstream action prediction for manipulation, and shows strong gains in both simulation and real-world tasks. This makes it a clear embodied robotics VAM paper rather than a peripheral foundation model work.

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

### MVDP

**Paper:** [Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model](docs/papers/embodied_robotics/20260403_multi_view_video_diffusion_policy_a_3d_spatio_temporal_aware_video_action_model/paper_arxiv_code/README.md)  
**arXiv:** [2604.03181](https://arxiv.org/abs/2604.03181)

**Abstract:**  
Robotic manipulation requires understanding both the 3D spatial structure of the
environment and its temporal evolution, yet most existing policies overlook one or both.
They typically rely on 2D visual observations and backbones pretrained on static image--
text pairs, resulting in high data requirements and limited understanding of environment
dynamics. To address this, we introduce MV-VDP, a multi-view video diffusion policy that
jointly models the 3D spatio-temporal state of the environment. The core idea is to
simultaneously predict multi-view heatmap videos and RGB videos, which 1) align the
representation format of video pretraining with action finetuning, and 2) specify not
only what actions the robot should take, but also how the environment is expected to
evolve in response to those actions. Extensive experiments show that MV-VDP enables
data-efficient, robust, generalizable, and interpretable manipulation. With only ten
demonstration trajectories and without additional pretraining, MV-VDP successfully
performs complex real-world tasks, demonstrates strong robustness across a range of
model hyperparameters, generalizes to out-of-distribution settings, and predicts
realistic future videos. Experiments on Meta-World and real-world robotic platforms
demonstrate that MV-VDP consistently outperforms video-prediction--based, 3D-based, and
vision--language--action models, establishing a new state of the art in data-efficient
multi-task manipulation.

### PRWM

**Paper:** [Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning](docs/papers/embodied_robotics/20260326_persistent_robot_world_models_stabilizing_multi_step_rollouts_via_reinforcement_learning/paper_arxiv_code/README.md)  
**arXiv:** [2603.25685](https://arxiv.org/abs/2603.25685)

**Abstract:**  
Action-conditioned robot world models generate future video frames of the manipulated
scene given a robot action sequence, offering a promising alternative for simulating
tasks that are difficult to model with traditional physics engines. However, these
models are optimized for short-term prediction and break down when deployed
autoregressively: each predicted clip feeds back as context for the next, causing errors
to compound and visual quality to rapidly degrade. We address this through the following
contributions. First, we introduce a reinforcement learning (RL) post-training scheme
that trains the world model on its own autoregressive rollouts rather than on ground-
truth histories. We achieve this by adapting a recent contrastive RL objective for
diffusion models to our setting and show that its convergence guarantees carry over
exactly. Second, we design a training protocol that generates and compares multiple
candidate variable-length futures from the same rollout state, reinforcing higher-
fidelity predictions over lower-fidelity ones. Third, we develop efficient, multi-view
visual fidelity rewards that combine complementary perceptual metrics across camera
views and are aggregated at the clip level for dense, low-variance training signal.
Fourth, we show that our approach establishes a new state-of-the-art for rollout
fidelity on the DROID dataset, outperforming the strongest baseline on all metrics
(e.g., LPIPS reduced by 14% on external cameras, SSIM improved by 9.1% on the wrist
camera), winning 98% of paired comparisons, and achieving an 80% preference rate in a
blind human study.

### DWAM

**Paper:** [Do World Action Models Generalize Better than VLAs? A Robustness Study](docs/papers/embodied_robotics/20260323_do_world_action_models_generalize_better_than_vlas_a_robustness_study/paper_arxiv_code/README.md)  
**arXiv:** [2603.22078](https://arxiv.org/abs/2603.22078)

**Abstract:**  
Robot action planning in the real world is challenging as it requires not only
understanding the current state of the environment but also predicting how it will
evolve in response to actions. Vision-language-action (VLA), which repurpose large-scale
vision-language models for robot action generation using action experts, have achieved
notable success across a variety of robotic tasks. Nevertheless, their performance
remains constrained by the scope of their training data, exhibiting limited
generalization to unseen scenarios and vulnerability to diverse contextual
perturbations. More recently, world models have been revisited as an alternative to
VLAs. These models, referred to as world action models (WAMs), are built upon world
models that are trained on large corpora of video data to predict future states. With
minor adaptations, their latent representation can be decoded into robot actions. It has
been suggested that their explicit dynamic prediction capacity, combined with
spatiotemporal priors acquired from web-scale video pretraining, enables WAMs to
generalize more effectively than VLAs. In this paper, we conduct a comparative study of
prominent state-of-the-art VLA policies and recently released WAMs. We evaluate their
performance on the LIBERO-Plus and RoboTwin 2.0-Plus benchmarks under various visual and
language perturbations. Our results show that WAMs achieve strong robustness, with
LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and Cosmos-Policy achieving
82.2% on LIBERO-Plus. While VLAs such as $π_{0.5}$ can achieve comparable robustness on
certain tasks, they typically require extensive training with diverse robotic datasets
and varied learning objectives. Hybrid approaches that partially incorporate video-based
dynamic learning exhibit intermediate robustness, highlighting the importance of how
video priors are integrated.

### VAMPO

**Paper:** [VAMPO: Policy Optimization for Improving Visual Dynamics in Video Action Models](docs/papers/embodied_robotics/20260319_vampo_policy_optimization_for_improving_visual_dynamics_in_video_action_models/paper_arxiv_code/README.md)  
**arXiv:** [2603.19370](https://arxiv.org/abs/2603.19370)

**Abstract:**  
Video action models are an appealing foundation for Vision--Language--Action systems
because they can learn visual dynamics from large-scale video data and transfer this
knowledge to downstream robot control. Yet current diffusion-based video predictors are
trained with likelihood-surrogate objectives, which encourage globally plausible
predictions without explicitly optimizing the precision-critical visual dynamics needed
for manipulation. This objective mismatch often leads to subtle errors in object pose,
spatial relations, and contact timing that can be amplified by downstream policies. We
propose VAMPO, a post-training framework that directly improves visual dynamics in video
action models through policy optimization. Our key idea is to formulate multi-step
denoising as a sequential decision process and optimize the denoising policy with
rewards defined over expert visual dynamics in latent space. To make this optimization
practical, we introduce an Euler Hybrid sampler that injects stochasticity only at the
first denoising step, enabling tractable low-variance policy-gradient estimation while
preserving the coherence of the remaining denoising trajectory. We further combine this
design with GRPO and a verifiable non-adversarial reward. Across diverse simulated and
real-world manipulation tasks, VAMPO improves task-relevant visual dynamics, leading to
better downstream action generation and stronger generalization. The homepage is
https://vampo-robot.github.io/VAMPO/.


## Autonomous Driving

### Epona

**Paper:** [Epona: Autoregressive Diffusion World Model for Autonomous Driving](docs/papers/autonomous_driving/20250630_epona_autoregressive_diffusion_world_model_for_autonomous_driving/paper_arxiv_code/README.md)  
**arXiv:** [2506.24113](https://arxiv.org/abs/2506.24113)

**Abstract:**  
Epona is a core autonomous-driving world model paper built around autoregressive diffusion. Instead of treating future video prediction and motion planning as separate modules, it factorizes temporal dynamics and future-world generation while coupling trajectory prediction with visual modeling inside one end-to-end framework. The model is designed for long-horizon, flexible-length rollout and explicitly positions the learned world model as a real-time motion planner, which puts it squarely in the driving-side WAM line rather than in a peripheral video-generation category.

### World4Drive

**Paper:** [World4Drive: End-to-End Autonomous Driving via Intention-aware Physical Latent World Model](docs/papers/autonomous_driving/20250701_world4drive_end_to_end_autonomous_driving_via_intention_aware_physical_latent_world_model/paper_arxiv_code/README.md)  
**arXiv:** [2507.00603](https://arxiv.org/abs/2507.00603)

**Abstract:**  
World4Drive is a driving-side latent world model for end-to-end planning. It builds intention-aware and physically grounded latent scene representations, generates multiple candidate planning trajectories, predicts intention-driven future latent states, and then uses a selector to choose the best plan. Although it emphasizes latent physical world modeling more than explicit video-action naming, it clearly belongs to the autonomous-driving WAM line because the learned world model is directly used for future-state reasoning and trajectory planning rather than only as an auxiliary supervision signal.

### DriveLaW

**Paper:** [DriveLaW: Unifying Planning and Video Generation in a Latent Driving World](docs/papers/autonomous_driving/20251229_drivelaw_unifying_planning_and_video_generation_in_a_latent_driving_world/paper_arxiv_code/README.md)  
**arXiv:** [2512.23421](https://arxiv.org/abs/2512.23421)

**Abstract:**  
DriveLaW unifies future video generation and motion planning inside one latent driving-world framework. Its core idea is to inject the latent representation of a high-fidelity driving video generator directly into a diffusion-based planner, so the imagined future and the resulting planned trajectory stay consistent by construction rather than through loose inter-module coupling. This makes it a clear autonomous-driving WAM/VAM paper: the world model is not only forecasting the future but is structurally tied to trajectory planning and benchmarked on both video prediction and NAVSIM planning.

### DriveVA

**Paper:** [DriveVA: Video Action Models are Zero-Shot Drivers](docs/papers/autonomous_driving/20260405_driveva_video_action_models_are_zero_shot_drivers/paper_arxiv_code/README.md)  
**arXiv:** [2604.04198](https://arxiv.org/abs/2604.04198)

**Abstract:**  
DriveVA studies autonomous driving through a video-action world model that jointly generates future scene videos and action trajectories in one shared latent process. Instead of treating visual forecasting and planning as loosely coupled modules, it uses a DiT-based decoder to align trajectory planning with future scene evolution more tightly. By inheriting priors from large-scale video generation models, DriveVA improves generalization across unseen domains and sensor setups, and shows strong zero-shot driving performance on NAVSIM, nuScenes, and Bench2Drive.

## Foundational Works

### SERL

**Paper:** [SERL: A Software Suite for Sample-Efficient Robotic Reinforcement Learning](docs/papers/foundational_works/20240129_serl_a_software_suite_for_sample_efficient_robotic_reinforcement_learning/paper_arxiv_code/README.md)  
**arXiv:** [2401.16013](https://arxiv.org/abs/2401.16013)

**Abstract:**  
SERL is a foundational robotics RL systems paper rather than a WAM paper itself. It packages a carefully engineered, sample-efficient off-policy reinforcement learning stack for real-world robot learning, together with reward computation, reset strategies, controller support, and challenging benchmark tasks. It is relevant here because later world-model and VLA lines frequently rely on the same broader practical question: how to make real-robot learning robust, efficient, and reproducible outside pure simulation.

### LAPA

**Paper:** [Latent Action Pretraining from Videos](docs/papers/foundational_works/20241015_latent_action_pretraining_from_videos/paper_arxiv_code/README.md)  
**arXiv:** [2410.11758](https://arxiv.org/abs/2410.11758)

**Abstract:**  
LAPA introduces Latent Action Pretraining for general Action models, an unsupervised way to pretrain VLA systems without ground-truth robot action labels. Its key idea is to use frame-to-frame visual change as an implicit action signal: first learning discrete latent actions between image frames with a VQ-VAE-style action quantization model, then training a latent VLA to predict those latent actions from observations and language, and finally fine-tuning on a smaller amount of robot data to map latent actions to executable controls. This makes LAPA better treated as a foundational latent-action precursor for later WAM work rather than as a WAM paper itself.

### HIL-SERL

**Paper:** [Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](docs/papers/foundational_works/20241029_precise_and_dexterous_robotic_manipulation_via_human_in_the_loop_reinforcement_learning/paper_arxiv_code/README.md)  
**arXiv:** [2410.21845](https://arxiv.org/abs/2410.21845)

**Abstract:**  
HIL-SERL extends the SERL line with human-in-the-loop reinforcement learning for more precise and dexterous real-world manipulation. It combines demonstrations, human corrections, efficient RL, and system-level design choices to train robust policies for dynamic manipulation, precision assembly, and dual-arm coordination in practical real-world time budgets. It belongs in foundational works because it is an important precursor in real-robot learning infrastructure and data-collection methodology, not because it is itself a WAM/VAM paper.

### pi0

**Paper:** [$π_0$: A Vision-Language-Action Flow Model for General Robot Control](docs/papers/foundational_works/20241031_0_a_vision_language_action_flow_model_for_general_robot_control/paper_arxiv_code/README.md)  
**arXiv:** [2410.24164](https://arxiv.org/abs/2410.24164)

**Abstract:**  
$π_0$ is a major generalist VLA foundation model built with a flow-matching action architecture on top of a pretrained vision-language backbone. It targets general robot control across diverse embodiments and tasks, emphasizing semantic transfer, broad pretraining, and dexterous manipulation. It is best treated as foundational work here because many later WAM/VAM papers position themselves against, extend, or compare to the `pi` line even though $π_0$ itself is not a world-action model.

### pi0.5

**Paper:** [π0.5: a Vision-Language-Action Model with Open-World Generalization](docs/papers/foundational_works/20250401_pi0_5_a_vision_language_action_model_with_open_world_generalization/paper_arxiv_code/README.md)  
**Source:** [Physical Intelligence blog](https://www.pi.website/blog/pi05)

**Abstract:**  
π0.5 extends the `pi` VLA line toward stronger open-world generalization by co-training across heterogeneous robot, semantic, and web-scale data sources. The model is designed to transfer knowledge across embodiments, high-level prediction tasks, and messy real-world environments, pushing beyond lab-style evaluation. It fits foundational works because it is a highly influential VLA baseline and comparison target for later WAM/VAM methods, not because it directly performs action-conditioned future world modeling.

### pi0.6

**Paper:** [$π^{*}_{0.6}$: a VLA That Learns From Experience](docs/papers/foundational_works/20251118_0_6_a_vla_that_learns_from_experience/paper_arxiv_code/README.md)  
**arXiv:** [2511.14759](https://arxiv.org/abs/2511.14759)

**Abstract:**  
$π^{*}_{0.6}$ studies how VLA models can improve from real-world deployment through reinforcement learning. It introduces the RECAP training method, which combines offline RL pretraining, on-policy experience, demonstrations, and expert teleoperated interventions to let a generalist VLA improve through experience. This belongs in foundational works because it is part of the influential `pi` family and shapes the broader embodied policy landscape that WAM/VAM papers are compared against.

### RL-Token

**Paper:** [Precise Manipulation with Efficient Online RL](docs/papers/foundational_works/20260319_precise_manipulation_with_efficient_online_rl/paper_arxiv_code/README.md)  
**Source:** [Physical Intelligence research page](https://www.pi.website/research/rlt)

**Abstract:**  
RL-Token studies how to attach a lightweight online reinforcement-learning module to a pretrained VLA without fine-tuning the full model. Its key idea is to train the VLA to emit a compact RL token that summarizes the model's internal state, then use that token as the input to small actor and critic networks that can be updated on-robot in real time. This makes it possible to improve precise, contact-rich phases of manipulation tasks with only minutes or hours of real-world data. It belongs in foundational works because it is a `pi`-line method for experience-based adaptation of VLA policies rather than a direct WAM/VAM paper.
