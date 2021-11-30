# Copyright (c) OpenMMLab. All rights reserved.
runner = dict(
    name='Debug CamRunner',
    camera_id=0,
    display_delay=0,
    frame_buffer_size=20,
    user_buffers=[('det_result', 1), ('pose_result', 1)],
    nodes=[
        dict(
            type='DetectorNode',
            name='detector',
            model_config='demo/mmdetection_cfg/'
            'ssdlite_mobilenetv2_scratch_600e_coco.py',
            model_checkpoint='https://download.openmmlab.com'
            '/mmdetection/v2.0/ssd/'
            'ssdlite_mobilenetv2_scratch_600e_coco/ssdlite_mobilenetv2_'
            'scratch_600e_coco_20210629_110627-974d9307.pth',
            input_buffer='_input_',
            output_buffer='det_result'),
        dict(
            type='TopDownPoseEstimatorNode',
            name='human pose estimator',
            model_config='configs/wholebody/2d_kpt_sview_rgb_img/'
            'topdown_heatmap/coco-wholebody/'
            'vipnas_res50_coco_wholebody_256x192_dark.py',
            model_checkpoint='https://openmmlab-share.oss-cn-hangzhou'
            '.aliyuncs.com/mmpose/top_down/vipnas/'
            'vipnas_res50_wholebody_256x192_dark-67c0ce35_20211112.pth',
            cls_names=['person'],
            input_buffer='det_result',
            output_buffer='pose_result'),
        dict(
            type='PoseVisualizerNode',
            name='visualizer',
            frame_buffer='_frame_',
            result_buffer='pose_result',
            output_buffer='_display_')
    ])
