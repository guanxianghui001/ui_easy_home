/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 80033 (8.0.33)
 Source Host           : 172.20.101.33:3306
 Source Schema         : ui_easy_home

 Target Server Type    : MySQL
 Target Server Version : 80033 (8.0.33)
 File Encoding         : 65001

 Date: 29/06/2023 15:23:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for code_detail
-- ----------------------------
DROP TABLE IF EXISTS `code_detail`;
CREATE TABLE `code_detail`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增，不做他用',
  `code_type_id` int NOT NULL COMMENT '使用类型id',
  `code_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '使用类型',
  `code_value` int NOT NULL COMMENT '使用类型子id',
  `code_desc` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '描述信息',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`, `code_value`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 50 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '预置码值表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of code_detail
-- ----------------------------
# INSERT INTO `code_detail` VALUES (1, 1, '步骤类型', 101, '浏览器操作');
# INSERT INTO `code_detail` VALUES (2, 1, '步骤类型', 102, '弹窗操作');
# INSERT INTO `code_detail` VALUES (3, 1, '步骤类型', 103, '元素操作');
# INSERT INTO `code_detail` VALUES (4, 1, '步骤类型', 104, '鼠标操作');
# INSERT INTO `code_detail` VALUES (5, 1, '步骤类型', 105, '流程控制');
# INSERT INTO `code_detail` VALUES (6, 101, '浏览器操作类型', 1011, '打开网页');
# INSERT INTO `code_detail` VALUES (7, 101, '浏览器操作类型', 1012, '关闭网页');
# INSERT INTO `code_detail` VALUES (8, 101, '浏览器操作类型', 1013, '切换窗口');
# INSERT INTO `code_detail` VALUES (9, 101, '浏览器操作类型', 1014, '设置窗口大小');
# INSERT INTO `code_detail` VALUES (10, 103, '元素操作类型', 1031, '提交表单');
# INSERT INTO `code_detail` VALUES (11, 103, '元素操作类型', 1032, '下拉框操作');
# INSERT INTO `code_detail` VALUES (12, 103, '元素操作类型', 1033, '设置选项');
# INSERT INTO `code_detail` VALUES (13, 103, '元素操作类型', 1034, '等待元素');
# INSERT INTO `code_detail` VALUES (14, 104, '鼠标操作类型', 1041, '鼠标点击');
# INSERT INTO `code_detail` VALUES (15, 104, '鼠标操作类型', 1042, '鼠标移动');
# INSERT INTO `code_detail` VALUES (16, 104, '鼠标操作类型', 1043, '鼠标拖拽');
# INSERT INTO `code_detail` VALUES (17, 105, '流程控制类型', 1051, '次数循环');
# INSERT INTO `code_detail` VALUES (18, 1013, '切换窗口类型', 10131, '切换到初始窗口');
# INSERT INTO `code_detail` VALUES (19, 1013, '切换窗口类型', 10132, '根据网页索引号切换到指定窗口');
# INSERT INTO `code_detail` VALUES (20, 1014, '设置窗口大小类型', 10141, '窗口最大化');
# INSERT INTO `code_detail` VALUES (21, 1014, '设置窗口大小类型', 10142, '指定尺寸（像素为单位）');
# INSERT INTO `code_detail` VALUES (22, 2, '元素定位类型', 201, 'id');
# INSERT INTO `code_detail` VALUES (23, 2, '元素定位类型', 202, 'name');
# INSERT INTO `code_detail` VALUES (24, 2, '元素定位类型', 203, 'classname');
# INSERT INTO `code_detail` VALUES (25, 2, '元素定位类型', 204, 'tagname');
# INSERT INTO `code_detail` VALUES (26, 2, '元素定位类型', 205, 'linktext');
# INSERT INTO `code_detail` VALUES (27, 2, '元素定位类型', 206, 'xpath');
# INSERT INTO `code_detail` VALUES (28, 2, '元素定位类型', 207, 'label');
# INSERT INTO `code_detail` VALUES (29, 2, '元素定位类型', 208, 'value');
# INSERT INTO `code_detail` VALUES (30, 2, '元素定位类型', 209, 'index');
# INSERT INTO `code_detail` VALUES (31, 2, '元素定位类型', 2010, 'css');
# INSERT INTO `code_detail` VALUES (32, 3, '前置操作类型', 301, '等待时间');
# INSERT INTO `code_detail` VALUES (33, 3, '前置操作类型', 302, '截图');
# INSERT INTO `code_detail` VALUES (34, 4, '后置操作类型', 401, '等待时间');
# INSERT INTO `code_detail` VALUES (35, 4, '后置操作类型', 402, '断言');
# INSERT INTO `code_detail` VALUES (36, 4, '后置操作类型', 403, '截图');
# INSERT INTO `code_detail` VALUES (37, 402, '断言类型', 4021, '元素断言');
# INSERT INTO `code_detail` VALUES (38, 402, '断言类型', 4022, '弹窗文本');
# INSERT INTO `code_detail` VALUES (39, 402, '断言类型', 4023, '网页标题');
# INSERT INTO `code_detail` VALUES (40, 4021, '断言方式类型', 40211, '元素被选中');
# INSERT INTO `code_detail` VALUES (41, 4021, '断言方式类型', 40212, '元素可编辑');
# INSERT INTO `code_detail` VALUES (42, 4021, '断言方式类型', 40213, '元素存在');
# INSERT INTO `code_detail` VALUES (43, 4021, '断言方式类型', 40214, '元素不存在');
# INSERT INTO `code_detail` VALUES (44, 4021, '断言方式类型', 40215, '元素未被选中');
# INSERT INTO `code_detail` VALUES (45, 4021, '断言方式类型', 40216, '元素不可编辑');
# INSERT INTO `code_detail` VALUES (46, 4021, '断言方式类型', 40217, '元素文本不等于期望值');
# INSERT INTO `code_detail` VALUES (47, 4021, '断言方式类型', 40218, '元素文本等于期望值');
# INSERT INTO `code_detail` VALUES (48, 4021, '断言方式类型', 40219, '元素文本不包含期望值');
# INSERT INTO `code_detail` VALUES (49, 4021, '断言方式类型', 402110, '元素文本包含期望值');

-- ----------------------------
-- Table structure for element
-- ----------------------------
DROP TABLE IF EXISTS `element`;
CREATE TABLE `element`  (
  `id` bigint NOT NULL COMMENT '元素id',
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '元素名称',
  `module_id` bigint NOT NULL COMMENT '模块id',
  `location_type` int NOT NULL COMMENT '定位类型',
  `location` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '元素定位',
  `target_location` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '其他备用填写文本或定位',
  `desc` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '描述信息',
  `project_id` bigint NOT NULL COMMENT '项目id',
  `is_del` tinyint NOT NULL COMMENT '是否删除，删除为0，有效为1',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '元素表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of element
-- ----------------------------

-- ----------------------------
-- Table structure for module
-- ----------------------------
DROP TABLE IF EXISTS `module`;
CREATE TABLE `module`  (
  `id` int NOT NULL COMMENT '模块id',
  `name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '模块名称',
  `father_node_id` bigint NOT NULL COMMENT '模块父节点id',
  `level` tinyint NULL DEFAULT NULL COMMENT '模块目录等级数，root为0级，root子节点为1，root孙节点为2，依此类推',
  `project_id` bigint NOT NULL COMMENT '项目id',
  `is_del` tinyint NULL DEFAULT NULL COMMENT '是否删除，删除为0，有效为1',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '模块表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for project
-- ----------------------------
DROP TABLE IF EXISTS `project`;
CREATE TABLE `project`  (
  `id` bigint UNSIGNED NOT NULL COMMENT '项目id',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '项目名称',
  `is_del` tinyint(3) UNSIGNED ZEROFILL NULL DEFAULT 000 COMMENT '是否删除，删除为0，有效为1',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '项目表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of project
-- ----------------------------

-- ----------------------------
-- Table structure for scenario
-- ----------------------------
DROP TABLE IF EXISTS `scenario`;
CREATE TABLE `scenario`  (
  `id` bigint NOT NULL COMMENT '场景id',
  `project_id` bigint NULL DEFAULT NULL COMMENT '项目id，与项目表关联',
  `module_id` bigint NULL DEFAULT NULL COMMENT '模块id，与模块表关联',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '场景名称',
  `status` tinyint NULL DEFAULT NULL COMMENT '场景状态，1为未开始，2为运行中，3为已完成',
  `step_total` tinyint NULL DEFAULT NULL COMMENT '步骤总数',
  `desc` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '描述',
  `is_del` tinyint NULL DEFAULT NULL COMMENT '是否删除，删除为0，有效为1',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '场景表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of scenario
-- ----------------------------

-- ----------------------------
-- Table structure for step
-- ----------------------------
DROP TABLE IF EXISTS `step`;
CREATE TABLE `step`  (
  `id` bigint NOT NULL COMMENT '步骤id',
  `scenario_id` bigint NOT NULL COMMENT '场景id，场景id存在后，拿着id在这个表中查找所有步骤',
  `step_type` int NULL DEFAULT NULL COMMENT '步骤类型，201浏览器操作、204鼠标操作、203元素操作',
  `operation_type` int NULL DEFAULT NULL COMMENT '操作类型，步骤下的子类型',
  `operation_object_id` bigint NULL DEFAULT NULL COMMENT '非操作元素id都放在这里',
  `element_type` tinyint NULL DEFAULT NULL COMMENT '元素类型，1为元素对象，2为元素定位，元素对象时，使用elementid去元素库查对应信息，元素定位时，location和locationtype不能为空',
  `element_id` bigint NULL DEFAULT NULL COMMENT '元素对象id',
  `location_type` int NULL DEFAULT NULL COMMENT '元素定位类型',
  `location` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '位置',
  `operation` int NULL DEFAULT NULL COMMENT '操作动作',
  `operation_text` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '操作文本，界面所有需要输入的本本，都存贮在这个字段中',
  `post_operation_type` int NULL DEFAULT NULL COMMENT '后置操作类型，目前只支持元素断言',
  `assert_type` int NULL DEFAULT NULL COMMENT '后置断言类型，元素断言中具体断言方式类型，603元素存在、604元素不存在、607元素文本等于期望值、608元素文本不等于期望值',
  `post_element_id` bigint NULL DEFAULT NULL COMMENT '后置元素id',
  `text` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '后置操作期望值',
  `order` int NOT NULL COMMENT '步骤排序，默认生成时，自动间隔1000',
  `is_del` tinyint NOT NULL COMMENT '是否删除，删除为0，有效为1',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '步骤表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of step
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
